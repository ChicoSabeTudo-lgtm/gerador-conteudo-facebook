"""
Módulo de Web Scraping para extração de conteúdo de notícias
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def scrape(self, url):
        """
        Extrai conteúdo de uma URL de notícia
        
        Args:
            url (str): URL da notícia
            
        Returns:
            dict: Dicionário com título, conteúdo e metadados
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extrai título
            title = self._extract_title(soup)
            
            # Extrai conteúdo principal
            content = self._extract_content(soup)
            
            # Extrai metadados
            description = self._extract_meta_description(soup)
            
            return {
                'success': True,
                'url': url,
                'title': title,
                'content': content,
                'description': description,
                'domain': urlparse(url).netloc
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Erro ao acessar URL: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Erro ao processar conteúdo: {str(e)}'
            }
    
    def _extract_title(self, soup):
        """Extrai o título da página"""
        # Tenta diferentes tags de título
        title_tags = [
            soup.find('h1'),
            soup.find('meta', property='og:title'),
            soup.find('meta', attrs={'name': 'twitter:title'}),
            soup.find('title')
        ]
        
        for tag in title_tags:
            if tag:
                if tag.name == 'meta':
                    return tag.get('content', '').strip()
                else:
                    return tag.get_text().strip()
        
        return 'Título não encontrado'
    
    def _extract_content(self, soup):
        """Extrai o conteúdo principal da notícia"""
        # Remove scripts, styles e outros elementos desnecessários
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            element.decompose()
        
        # Tenta encontrar o conteúdo principal
        content_selectors = [
            soup.find('article'),
            soup.find('div', class_=lambda x: x and ('content' in x.lower() or 'article' in x.lower())),
            soup.find('div', id=lambda x: x and ('content' in x.lower() or 'article' in x.lower())),
            soup.find('main')
        ]
        
        for selector in content_selectors:
            if selector:
                # Extrai parágrafos
                paragraphs = selector.find_all('p')
                if paragraphs:
                    text = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
                    if len(text) > 100:  # Verifica se tem conteúdo substancial
                        return text[:3000]  # Limita a 3000 caracteres
        
        # Fallback: pega todos os parágrafos da página
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        return text[:3000] if text else 'Conteúdo não encontrado'
    
    def _extract_meta_description(self, soup):
        """Extrai a meta description"""
        meta_tags = [
            soup.find('meta', attrs={'name': 'description'}),
            soup.find('meta', property='og:description'),
            soup.find('meta', attrs={'name': 'twitter:description'})
        ]
        
        for tag in meta_tags:
            if tag and tag.get('content'):
                return tag.get('content').strip()
        
        return ''

