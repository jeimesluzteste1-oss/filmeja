# 🎬 FilmeJá — Guia de Conexão na Vercel & Domínio Hostinger

Este guia mostra exatamente o que você precisa fazer para colocar o **FilmeJá** no ar em produção no domínio **`filmeja.com.br`** e como funciona a esteira de publicações automáticas.

---

## 🚀 PASSO 1: Como colocar o projeto na Vercel (2 Minutos)

A Vercel é a plataforma oficial dos criadores do Next.js. Ela oferece CDN global ultrarrápida, SSL (HTTPS) gratuito e deploys automáticos a cada novo post.

### Opção A (A mais fácil e recomendada): Via GitHub
1. Crie um repositório no seu GitHub (ex: `filmeja`).
2. No terminal desta pasta, vincule e suba os arquivos:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/filmeja.git
   git push -u origin main
   ```
3. Acesse **[vercel.com](https://vercel.com)**, faça login com seu GitHub.
4. Clique em **"Add New..." → "Project"**.
5. Selecione o repositório **`filmeja`** e clique em **"Deploy"**.
6. Pronto! Em 40 segundos o site já estará no ar com um link temporário (ex: `filmeja.vercel.app`).

### Opção B: Direto pelo Terminal (Sem GitHub)
Se preferir subir direto pelo terminal:
```bash
npx vercel
```
O assistente vai abrir o navegador para você logar na Vercel e já faz o deploy sozinho.

---

## 🌐 PASSO 2: Como Conectar o Domínio `filmeja.com.br` na Vercel

Depois de criar o projeto na Vercel:

### 1. Adicionar o domínio na Vercel
1. No painel do seu projeto na Vercel, vá na aba **Settings** (Configurações) → **Domains**.
2. Digite: `filmeja.com.br` e clique em **Add**.
3. A Vercel vai sugerir adicionar também o `www.filmeja.com.br` com redirecionamento automático (clique para aceitar).
4. A tela da Vercel vai mostrar exatamente os 2 registros DNS necessários:
   - **Registro A:** `@` apontando para `76.76.21.21`
   - **Registro CNAME:** `www` apontando para `cname.vercel-dns.com`

---

### 2. Configurar o DNS no painel da Hostinger
1. Acesse o **hPanel da Hostinger** ([hpanel.hostinger.com](https://hpanel.hostinger.com)).
2. Clique no menu **Domínios** e clique em **`filmeja.com.br`**.
3. No menu lateral esquerdo, clique em **DNS / Servidores de Nomes**.
4. **Altere ou Adicione os 2 registros:**
   
| Tipo | Nome | Aponta para (Valor) | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `76.76.21.21` | 3600 (ou padrão) |
| **CNAME** | `www` | `cname.vercel-dns.com` | 3600 (ou padrão) |

*(Se já existirem registros antigos do tipo A apontando para `2.57.91.91`, basta editar ou excluir).*

5. Salve as alterações. Em poucos minutos, a Vercel vai detectar a conexão, emitir o certificado SSL verde (HTTPS) e o **`filmeja.com.br`** estará ativo!

---

## 🤖 PASSO 3: Como Rodar a Automação Diária de Posts

Criamos o robô em Python (`scripts/gerador_filmeja.py`) pronto para gerar artigos de alta densidade em SEO.

### Para gerar uma nova lista Top 5:
```bash
python scripts/gerador_filmeja.py --tipo lista --tema "filmes de ficcao cientifica e suspense" --genero "Sci-Fi"
```

### Para gerar uma lista de Terror:
```bash
python scripts/gerador_filmeja.py --tipo lista --tema "filmes de terror com reviravolta" --genero "Terror"
```

O script:
1. Cria a publicação formatada com título magnético, sinopses, avaliações, onde assistir e **Perguntas Frequentes (FAQ)**.
2. Salva o arquivo diretamente dentro de `src/content/posts/`.
3. Atualiza o relatório `resultado_YYYY-MM-DD.json`.
4. Quando você dá `git push`, a Vercel detecta o novo post e atualiza o site e o `sitemap.xml` em segundos!

---

## 🏆 O Arsenal de SEO Técnico já Ativo no Projeto

1. **Rich Snippets Automáticos:**
   - **Schema `ItemList`**: Para o Google listar seus Top 5 em carrossel.
   - **Schema `Movie` e `Review`**: Para exibir estrelas de avaliação e nota nos resultados de pesquisa.
   - **Schema `FAQPage`**: Cria as caixinhas de perguntas expansíveis direto na página do Google.
2. **Sitemap Dinâmico:** Disponível em `/sitemap.xml` para enviar no Google Search Console.
3. **Páginas de Categoria Otimizadas:** `/genero/terror`, `/genero/suspense` para capturar tráfego de cauda longa.
4. **Performance 100%:** HTML pré-renderizado estaticamente (SSG) com Core Web Vitals perfeitos para o algoritmo mobile do Google.
