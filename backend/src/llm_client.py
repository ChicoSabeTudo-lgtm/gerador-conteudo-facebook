"""
Cliente para integração com OpenAI API
"""
import os
import json
from openai import OpenAI

class LLMClient:
    def __init__(self):
        # A API key já está configurada na variável de ambiente OPENAI_API_KEY
        self.client = OpenAI()
        self.model = "gpt-4.1-mini"  # Modelo disponível no ambiente
    
    def generate_content(self, prompt):
        """
        Gera conteúdo usando a API OpenAI
        
        Args:
            prompt (str): Prompt formatado
            
        Returns:
            dict: Resposta estruturada da API
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um especialista em estratégia de conteúdo para redes sociais, com foco em Facebook. Sempre responda com JSON válido e estruturado."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000,
                response_format={"type": "json_object"}
            )
            
            # Extrai o conteúdo da resposta
            content = response.choices[0].message.content
            
            # Parse do JSON
            parsed_content = json.loads(content)
            
            return {
                'success': True,
                'data': parsed_content
            }
            
        except json.JSONDecodeError as e:
            return {
                'success': False,
                'error': f'Erro ao processar resposta JSON: {str(e)}',
                'raw_response': content if 'content' in locals() else None
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Erro ao gerar conteúdo: {str(e)}'
            }

