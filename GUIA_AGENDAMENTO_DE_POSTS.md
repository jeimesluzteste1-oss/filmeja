# ⏰ GUIA DE AGENDAMENTO AUTOMÁTICO DE POSTS — FILMEJÁ (2026)

Este guia explica como produzir múltiplos artigos de uma só vez (ex: 5, 10 ou 20 posts) e deixá-los **agendados para publicação automática**, garantindo que o seu site receba conteúdo novo todo santo dia sem você precisar sentar no computador diariamente.

---

## 🎯 1. Por que Agendar Posts é uma Mina de Ouro para SEO?

O algoritmo do Google adora **consistência**. 
- Se você publica 20 posts em 1 único dia e depois passa 2 semanas sem publicar nada, o Google rastreia o site uma vez e diminui a frequência de rastreamento.
- Mas se você publica **1 a 2 posts por dia, todos os dias no mesmo horário**, o robô do Google (Googlebot) passa a visitar o `filmeja.com.br` **várias vezes ao dia**, acelerando drasticamente a indexação de novas páginas e subindo suas posições no Search Console!

---

## 🏗️ 2. Como Funciona a Fila de Agendamento do FilmeJá

O sistema utiliza duas pastas organizadas:

1. **`src/content/posts/`**: São os artigos ativos no ar em produção agora.
2. **`src/content/agendados/`**: É a sua fila de espera. Os artigos ficam prontos, formatados, com imagens e tags, aguardando o dia e hora programados.

Quando a data programada chega:
O script `scripts/agendador.py` detecta que o horário venceu, move o arquivo para `src/content/posts/` e dispara o deploy para o GitHub e Vercel automaticamente!

---

## 🚀 3. Como Usar o Agendador via Linha de Comando

### Ver a fila de posts agendados:
```bash
python scripts/agendador.py --listar
```

### Agendar um post para daqui a X dias:
```bash
# Agenda o post gerado para sair daqui a 1 dia (amanhã às 09h)
python scripts/agendador.py --agendar-arquivo "src/content/posts/meu-post.json" --dias-a-frente 1

# Agenda para daqui a 3 dias
python scripts/agendador.py --agendar-arquivo "src/content/posts/outro-post.json" --dias-a-frente 3
```

### Publicar automaticamente os posts cuja data já chegou:
```bash
python scripts/agendador.py --verificar
```

---

## 🤖 4. Automação 100% na Nuvem (GitHub Actions Gratuito)

Você não precisa nem ligar o computador para publicar os posts agendados!
Criamos o fluxo do **GitHub Actions** em `.github/workflows/publicar_agendados.yml`.

Ele roda automaticamente **todos os dias às 09:00 da manhã**:
1. O GitHub acorda na nuvem.
2. Executa `python scripts/agendador.py --verificar`.
3. Se houver post cuja data chegou hoje, ele comita no repositório.
4. A Vercel detecta o commit e coloca o novo post no ar em 30 segundos!

---

## 📺 5. As Séries Mais Quentes em Alta para Agendar Esta Semana

Fizemos uma pesquisa detalhada sobre o que o público brasileiro está buscando no Google com a intenção *"Que dia sai o episódio?"* e lançamentos imediatos:

| Série | Plataforma | Formato de Exibição | Dia & Horário no Brasil | Status / Gancho de Busca |
| :--- | :--- | :--- | :--- | :--- |
| **O Pinguim (The Penguin)** | Max / HBO | Semanal | **Domingos às 22h** | 🔥 Maior audiência da HBO no momento. Recorde de buscas por *"que dia sai o novo episódio de O Pinguim"*. |
| **Matéria Escura (Dark Matter)** | Apple TV+ | Semanal | **Quartas-feiras às 22h** | 🌌 Sci-fi aclamado da Apple. Episódios com ganchos quânticos e alta retenção. |
| **Ruptura (Severance) — 2ª Temp.** | Apple TV+ | Semanal | **Sextas-feiras às 05h** | ⏳ Uma das voltas mais aguardadas do streaming mundial. Milhares de buscas diárias por data de estreia. |
| **Silô (Silo) — 2ª Temp.** | Apple TV+ | Semanal | **Sextas-feiras às 05h** | 🚪 Distopia subterrânea de enorme sucesso com Rebecca Ferguson. |
| **Duna: A Profecia** | Max | Semanal | **Domingos às 22h** | 🪐 Spin-off oficial do universo de Duna com foco na irmandade Bene Gesserit. |
| **Arcane — 2ª Temp.** | Netflix | Lançamento em 3 Atos | **Sábados às 05h** | ⚔️ Fenômeno mundial da Riot Games / Netflix lançado em blocos de episódios semanais. |

---

## 📝 6. Fluxo de Trabalho Recomendado: O Método "1 Dia de Trabalho = 10 Dias de Posts"

1. **Segunda-feira:** Você abre o `publicar_post.bat` e gera 5 a 10 artigos em sequência (leva cerca de 15 minutos).
2. Agenda cada um para os dias seguintes (terça, quarta, quinta, sexta...).
3. Roda `python scripts/gerador_threads.py` para gerar os textos das redes sociais correspondentes.
4. O site atualiza sozinho todos os dias e seu tráfego começa a crescer de forma consistente no Search Console!
