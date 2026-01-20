Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python com uso de IA Generativa para criar mensagens de marketing personalizadas para clientes de um banco fictício.

O objetivo é demonstrar o fluxo completo de dados — desde a extração de uma base CSV, passando por transformação com IA (OpenAI), até a carga dos resultados em arquivos locais — sem dependência de APIs externas indisponíveis.

Contexto do Problema:
  Como cientista de dados, o desafio consiste em:
  - Ler uma base de clientes a partir de um arquivo CSV
  - Gerar mensagens personalizadas incentivando investimentos
  - Associar essas mensagens a cada cliente
  - Persistir os resultados localmente

O projeto foi inspirado no Santander Dev Week 2023, adaptado para funcionar offline.

Pipeline ETL:
Etapa 1 - Extract:

  Fonte: arquivo CSV (data/users.csv)

  Dados extraídos:

  ID do usuário

  Nome

  Segmento

  Saldo

  Cidade

Etapa 2 - Transform:

  Geração de mensagens personalizadas via:

  OpenAI (GPT) – quando a variável OPENAI_API_KEY está configurada

  Modo mock – quando a API não está disponível

  As mensagens seguem regras:

  Curtas (≤ 120 caracteres)

  Linguagem clara e amigável

  Foco em educação financeira e investimentos

Etapa 3 - Load:

  Persistência local dos dados transformados:

  JSON (output/messages.json) — estrutura completa

  CSV (output/messages.csv) — formato tabular simplificado

Estrutura do Projeto:
  etl-ai-messages/
  
  data/
  -users.csv
  output/
  -messages.json
  -messages.csv
  src/
  -etl.py
  -prompt.py
  .env.example
  requirements.txt
  README.md

Tecnologias Utilizadas:

  Python 3.10+
  
  pandas
  
  OpenAI API
  
  python-dotenv
  
Como Executar:
  Instalar dependências
  pip install -r requirements.txt
  
  Configurar variáveis de ambiente
  cp .env.example .env


Edite o arquivo .env e insira sua chave da OpenAI:

  OPENAI_API_KEY=sua_api_key_aqui


Caso a chave não seja informada, o projeto será executado em modo mock.

Etapa 3 - Executar o pipeline:
python src/etl.py

Modo Mock (Sem IA)

  Quando a variável OPENAI_API_KEY não está definida:

  O pipeline continua funcionando

  As mensagens são geradas com texto padrão

  Ideal para testes e validação do fluxo ETL

Exemplo de Saída (CSV)
  user_id,name,segment,balance,city,message
  1,Naruto,Gold,1200.5,Sao Paulo,"Naruto, investir regularmente ajuda a construir segurança financeira."

Observações Importantes:

  Nenhum dado sensível real é utilizado
  
  As mensagens não prometem retorno financeiro
  
  O projeto tem fins educacionais e demonstrativos

Possíveis Evoluções:

  Persistência em banco de dados (SQLite/PostgreSQL)
  
  Cache de mensagens geradas
  
  Agendamento automático do pipeline
  
  Monitoramento e logs estruturados
  
  Integração com APIs reais

