import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Alert, AlertDescription } from '@/components/ui/alert.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Loader2, Link as LinkIcon, Copy, CheckCircle2, Facebook, Sparkles, FileText, MessageSquare } from 'lucide-react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [copiedItems, setCopiedItems] = useState({})

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!url.trim()) {
      setError('Por favor, insira uma URL válida')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)
    setCopiedItems({})

    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url.trim() }),
      })

      const data = await response.json()

      if (!response.ok || !data.success) {
        throw new Error(data.error || 'Erro ao gerar conteúdo')
      }

      setResult(data)
    } catch (err) {
      setError(err.message || 'Erro ao conectar com o servidor. Certifique-se de que o backend está rodando.')
    } finally {
      setLoading(false)
    }
  }

  const copyToClipboard = async (text, itemId) => {
    try {
      await navigator.clipboard.writeText(text)
      setCopiedItems(prev => ({ ...prev, [itemId]: true }))
      setTimeout(() => {
        setCopiedItems(prev => ({ ...prev, [itemId]: false }))
      }, 2000)
    } catch (err) {
      console.error('Erro ao copiar:', err)
    }
  }

  const CopyButton = ({ text, itemId, label = "Copiar" }) => (
    <Button
      variant="outline"
      size="sm"
      onClick={() => copyToClipboard(text, itemId)}
      className="gap-2"
    >
      {copiedItems[itemId] ? (
        <>
          <CheckCircle2 className="w-4 h-4 text-green-600" />
          Copiado!
        </>
      ) : (
        <>
          <Copy className="w-4 h-4" />
          {label}
        </>
      )}
    </Button>
  )

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <div className="container mx-auto px-4 py-8 max-w-7xl">
        {/* Header */}
        <div className="text-center mb-12 animate-fade-in">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Facebook className="w-12 h-12 text-blue-600" />
            <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              Gerador de Conteúdo
            </h1>
          </div>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Transforme qualquer notícia em títulos e posts otimizados para o Facebook
          </p>
          <p className="text-sm text-gray-500 mt-2">
            Otimizado para <span className="font-semibold text-blue-600">#ChicoSabeTudo</span>
          </p>
        </div>

        {/* Form */}
        <Card className="mb-8 shadow-xl border-2 hover:shadow-2xl transition-all duration-300">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <LinkIcon className="w-5 h-5" />
              Cole o link da notícia
            </CardTitle>
            <CardDescription>
              Insira a URL completa da notícia que você deseja transformar em conteúdo para Facebook
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="flex gap-3">
              <Input
                type="url"
                placeholder="https://exemplo.com/noticia"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                disabled={loading}
                className="flex-1 text-lg"
              />
              <Button 
                type="submit" 
                disabled={loading}
                className="px-8 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 transition-all duration-300"
              >
                {loading ? (
                  <>
                    <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                    Gerando...
                  </>
                ) : (
                  <>
                    <Sparkles className="mr-2 h-5 w-5" />
                    Gerar Conteúdo
                  </>
                )}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Error */}
        {error && (
          <Alert variant="destructive" className="mb-8 animate-fade-in">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6 animate-fade-in">
            {/* News Info */}
            <Card className="border-blue-200 bg-blue-50/50">
              <CardHeader>
                <CardTitle className="text-lg">📰 Notícia Analisada</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="font-semibold text-gray-800">{result.news_info.title}</p>
                <p className="text-sm text-gray-600 mt-1">{result.news_info.domain}</p>
              </CardContent>
            </Card>

            {/* Títulos */}
            <Card className="shadow-lg hover:shadow-xl transition-all duration-300">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-purple-700">
                  <FileText className="w-5 h-5" />
                  Sugestões de Títulos (15 opções)
                </CardTitle>
                <CardDescription>
                  3 seções com 5 títulos cada - escolha o que melhor se encaixa
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="diretos" className="w-full">
                  <TabsList className="grid w-full grid-cols-3">
                    <TabsTrigger value="diretos">Diretos</TabsTrigger>
                    <TabsTrigger value="perguntas">Perguntas</TabsTrigger>
                    <TabsTrigger value="engajamento">Engajamento</TabsTrigger>
                  </TabsList>
                  
                  <TabsContent value="diretos" className="space-y-3 mt-4">
                    <p className="text-sm text-gray-600 mb-3">
                      📋 <strong>Títulos Diretos e Informativos</strong> - Claros, objetivos e jornalísticos
                    </p>
                    {result.data.titulos.diretos.map((titulo, index) => (
                      <div key={index} className="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-200">
                        <p className="text-gray-800 flex-1">{index + 1}. {titulo}</p>
                        <CopyButton text={titulo} itemId={`direto-${index}`} />
                      </div>
                    ))}
                  </TabsContent>
                  
                  <TabsContent value="perguntas" className="space-y-3 mt-4">
                    <p className="text-sm text-gray-600 mb-3">
                      ❓ <strong>Títulos em Formato de Pergunta</strong> - Geram curiosidade e engajamento
                    </p>
                    {result.data.titulos.perguntas.map((titulo, index) => (
                      <div key={index} className="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-200">
                        <p className="text-gray-800 flex-1">{index + 1}. {titulo}</p>
                        <CopyButton text={titulo} itemId={`pergunta-${index}`} />
                      </div>
                    ))}
                  </TabsContent>
                  
                  <TabsContent value="engajamento" className="space-y-3 mt-4">
                    <p className="text-sm text-gray-600 mb-3">
                      💬 <strong>Títulos para Engajar</strong> - Geram interação, comentários e compartilhamentos
                    </p>
                    {result.data.titulos.engajamento.map((titulo, index) => (
                      <div key={index} className="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-200">
                        <p className="text-gray-800 flex-1">{index + 1}. {titulo}</p>
                        <CopyButton text={titulo} itemId={`engajamento-${index}`} />
                      </div>
                    ))}
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>

            {/* Posts */}
            <Card className="shadow-lg hover:shadow-xl transition-all duration-300">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-green-700">
                  <MessageSquare className="w-5 h-5" />
                  Posts para Facebook (3 opções)
                </CardTitle>
                <CardDescription>
                  Escolha o tom que melhor se adequa ao seu público
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="informativo" className="w-full">
                  <TabsList className="grid w-full grid-cols-3">
                    <TabsTrigger value="informativo">Informativo</TabsTrigger>
                    <TabsTrigger value="analitico">Analítico</TabsTrigger>
                    <TabsTrigger value="drama">Drama</TabsTrigger>
                  </TabsList>
                  
                  <TabsContent value="informativo" className="mt-4">
                    <div className="bg-blue-50 p-4 rounded-lg border border-blue-200 mb-3">
                      <p className="text-sm text-blue-700 font-semibold mb-2">
                        📢 Tom Informativo e Direto
                      </p>
                      <p className="text-xs text-blue-600">
                        Apresenta o fato de forma clara e objetiva. Ideal para quem quer se informar rapidamente.
                      </p>
                    </div>
                    <div className="bg-white p-6 rounded-lg border-2 border-blue-200 whitespace-pre-wrap">
                      {result.data.posts.informativo}
                    </div>
                    <div className="mt-4 flex justify-end">
                      <CopyButton 
                        text={result.data.posts.informativo} 
                        itemId="post-informativo"
                        label="Copiar Post Completo"
                      />
                    </div>
                  </TabsContent>
                  
                  <TabsContent value="analitico" className="mt-4">
                    <div className="bg-purple-50 p-4 rounded-lg border border-purple-200 mb-3">
                      <p className="text-sm text-purple-700 font-semibold mb-2">
                        🔍 Tom Analítico e Reflexivo
                      </p>
                      <p className="text-xs text-purple-600">
                        Explora o contexto, causas e consequências. Ideal para quem gosta de entender o "porquê".
                      </p>
                    </div>
                    <div className="bg-white p-6 rounded-lg border-2 border-purple-200 whitespace-pre-wrap">
                      {result.data.posts.analitico}
                    </div>
                    <div className="mt-4 flex justify-end">
                      <CopyButton 
                        text={result.data.posts.analitico} 
                        itemId="post-analitico"
                        label="Copiar Post Completo"
                      />
                    </div>
                  </TabsContent>
                  
                  <TabsContent value="drama" className="mt-4">
                    <div className="bg-red-50 p-4 rounded-lg border border-red-200 mb-3">
                      <p className="text-sm text-red-700 font-semibold mb-2">
                        🎭 Tom de Impacto e Drama
                      </p>
                      <p className="text-xs text-red-600">
                        Usa linguagem emocional para atrair pelo impacto. Ideal para público que acompanha pelo drama.
                      </p>
                    </div>
                    <div className="bg-white p-6 rounded-lg border-2 border-red-200 whitespace-pre-wrap">
                      {result.data.posts.drama}
                    </div>
                    <div className="mt-4 flex justify-end">
                      <CopyButton 
                        text={result.data.posts.drama} 
                        itemId="post-drama"
                        label="Copiar Post Completo"
                      />
                    </div>
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-12 text-gray-500 text-sm">
          <p>Desenvolvido com ❤️ para <span className="font-semibold">#ChicoSabeTudo</span></p>
        </div>
      </div>
    </div>
  )
}

export default App

