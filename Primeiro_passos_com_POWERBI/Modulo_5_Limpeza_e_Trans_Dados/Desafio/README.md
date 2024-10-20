# Análise de Dados de Colaboradores e Departamentos

## Descrição

Este projeto envolve a análise de dados de colaboradores e departamentos de uma empresa utilizando o Power BI. O objetivo é transformar, limpar e visualizar os dados para extrair insights sobre a estrutura organizacional.

## Estrutura do Projeto

1. **Conexão com o Banco de Dados**:
   - Utilização do MySQL Workbench para gerenciar o banco de dados.
   - Dados foram extraídos da tabela `employee` e `department`.

2. **Transformação de Dados**:
   - Verificação dos cabeçalhos e tipos de dados.
   - Conversão de valores monetários para o tipo double.
   - Verificação e análise de valores nulos:
     - Identificação de colaboradores sem gerente.
     - Verificação de departamentos sem gerente e preenchimento das lacunas.

3. **Análise de Projetos**:
   - Verificação do número de horas alocadas nos projetos.

4. **Junções e Mesclagens**:
   - Mescla das tabelas `employee` e `department` para criar uma tabela de colaboradores com os respectivos nomes dos departamentos.
   - Eliminação de colunas desnecessárias após a mesclagem.
   - Junção dos colaboradores e nomes dos gerentes.

5. **Preparação de Dados**:
   - Mesclagem das colunas de nome e sobrenome para uma única coluna representando o nome completo dos colaboradores.
   - Mesclagem de departamentos e localizações para criar combinações únicas.

6. **Agrupamento de Dados**:
   - Agrupamento dos dados para contar quantos colaboradores existem por gerente.

## Ferramentas Utilizadas

- **MySQL Workbench**: Para gerenciamento e manipulação do banco de dados.
- **Power BI**: Para análise de dados e criação de relatórios visuais.

## Como Usar

1. Clone este repositório.
2. Certifique-se de ter o MySQL Workbench e o Power BI instalados.
3. Conecte-se ao banco de dados no MySQL Workbench para visualizar e manipular os dados.
4. Abra o Power BI e conecte-se ao banco de dados para analisar e visualizar os dados transformados.

<!-- ## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações, entre em contato:
- Seu Nome: [seu_email@example.com](mailto:seu_email@example.com)

-->

