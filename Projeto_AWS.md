Data: 23 de janeiro de 2026 Empresa: Abstergo Industries Responsável: Tulio Meneghelli de Oliveira

Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Tulio Meneghelli de Oliveira. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos.

Descrição do Projeto
O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

Etapa 1:

Nome da ferramenta: S3 Intelligent-Tiering

Foco da ferramenta: Otimização automática de custos de armazenamento.

Descrição de caso de uso: Ideal para situações onde não se conhece previamente o padrão de acesso aos dados. A ferramenta move objetos automaticamente entre camadas de acesso frequente e infrequente, reduzindo custos sem intervenção manual.

Etapa 2:

Nome da ferramenta: Amazon EC2 Auto Scaling (com instâncias Spot)

Foco da ferramenta: Escalabilidade dinâmica e redução de custos computacionais.

Descrição de caso de uso: Implementação de políticas de scaling preditivo e dinâmico para ajustar a quantidade de instâncias EC2 conforme a demanda real, evitando gastos com capacidade ociosa e aproveitando preços reduzidos de instâncias Spot para cargas de trabalho tolerantes a falhas.

Etapa 3:

Nome da ferramenta: Amazon Aurora

Foco da ferramenta: Alta performance e redução de overhead operacional em bancos de dados.

Descrição de caso de uso: Substituição de bancos de dados tradicionais por um serviço que oferece patches automatizados, failover nativo e recuperação de desastres. A eficiência na replicação de dados em múltiplas Zonas de Disponibilidade reduz a necessidade de infraestruturas complexas e caras de backup manual.

Conclusão
A implementação de ferramentas na empresa Abstergo Industries tem como esperado a redução drástica de gastos com armazenamento de dados pouco acessados, a eliminação de desperdício em infraestrutura de computação e a diminuição de custos operacionais com manutenção de bancos de dados, o que aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa.

Anexos
Manual de configuração de Ciclo de Vida do S3

Guia de implementação de Grupos de Auto Scaling

Relatório de comparativo de custos: On-premise vs. AWS Aurora

Assinatura do Responsável pelo Projeto:

Tulio Meneghelli de Oliveira