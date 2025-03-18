# das-2-2025
Notes on AWS regarding the Development and Software Architecture II class


Trade-offs que a nuvem apoia:
* Paga apenas pelo que utilizar, ou seja, caso tenha demanda para 40 computadores em um único momento, exemplo: Blackfriday, é possível subir apenas nesse periodo, não sendo necessário a compra de 40 maquinas.
* Automatização de providenciamento de maquinas (IAC - Infraestructure as a code) -> Programar para subir novamente um servidor, subir e parar serviços, etc..
* Possível criar um template de maquina e utilizar para subir outra maquina com mais facilidade
* Possíbilidade tratar recursos como descartaveis, ou seja, qualquer hora você pode excluir o servidor e criar outro do ZERO.

# Acoplamento
* O que é: É algo que não é possível substituir tão facilmente.
* Melhor Prática: Deixar os serviçoes separados, ex: Uma maquina para Web Servers e outra para Application Servers.
  * Utilizar um Load Balancing (ELB) onde irá redistribuir a carga. Também faz a checagem se a maquina está OK antes de enviar o pacote.
  * Utilizar um duplo Load Balancing para ter redundancia caso o Load Balacing caia.

#Crie Serviços
Dica: Faça um desing de serviço e não de um servidor. Assim irá poder ser utilizado o serviço em qualquer servidor.
* Utilização de Containers ou serverless
* Ex:
* É possível subir um servidor no EC2 contendendo um HTML estático. Mas também posso subir o mesmo site no S3, o que eu não me preocupro com versões de windows, instaladores, etc...

# Escolher seu Banco de dados
* Um banco de dados SQL tem limitações quando de trata de escalabilidade Horizontal, sendo que ao escalar horizontal, as outras replicas são apenas Leitura
* Utilizar o NOSQL: Quando é necessário Performance extrema, e,quando não é possível definir as colunas da tabelas.(Ex: A Amazon, que vende x produtos e cada produto tem propriedades únicas, para modelar todas as colunas de caracteristicas teriam que ter um alter table a cada novo tipo de produto.
* Idependente do modelo, é de boa prática ter um outro banco de dados apenas sincronizando, que irá ser acionado caso o banco principal falhe.

# Escalabilidade Vertical: Aumentar recursos de Maquina. Aumentar Maquina = Escalabilidade Vertical
# Escalabilidade Horizontal: Replicar o banco de dados e dividir as operações.

# Otimização de Custo
* WErner Volgaels - The Frugal Architect - Documentação desenvolvida pelo CTO da AWS para economizar na arquitetura de uma aplicação na AWS.
  *  https://thefrugalarchitect.com/
  *   Computer Otimizar - Verifica se o computador está hiperdimencionado ou subdimencionado, porém o de graça utiliza apenas 14 dias. Versão paga tem historico full.
  *   Trust advaizor - Verifica se a aplicação é segura.
 
# Using Cache
* Utilizado para salvar conteudos mais próximo de usuário para otimizar o serviço. Ex: Um filme 4k da netflix, não é solicitado direto de Norte Virginia, é carregado no Estado ou em alguns casos na cidade que o usuário solicitou.

# Segurança
* Usar serviços gerenciados;
* Log de acessos para os recursos;
* Utilizar o principio de privilegio minimo.
* Isolar partes da sua infraestrutura;
* encriptografar dados em transito
* Utilizar ferramentos de multipla autenticação (MFA)
* Automatizar o deploy de suas aplicaçãos

# Infraestrutura Global da AWS
* Ver Informações sobre servidores da AWS: https://aws.amazon.com/pt/about-aws/global-infrastructure/
* Regiões: Cidades que possuem bunckers da AWS.
  * Pensar sempre em onde a maioria dos clientes irá acessar. Quando mais perto, mais rápido.7
  * É um conjunto de AZ's que ficam na Região
* AZ's:  Availability Zibes São um conjunto de Datacenter.
* Local zone: Roda serviços computacionais onde nao possúi AZ's. São "minis" datacenter que rodam aplicações.
* Wavelength Zone: Zonas da AWS que rodam em antes 5G

# Tipos de Acesso
* AWS CLI - Cliente - Acesso via interface\cmd
* AWS SDK - Aplicação - Uma aplicação que utiliza acesso a AWS
* AWS API - Requisição - Requisição no postman, ou utilizando um software

# RBAC
* Role Base Access Control - 

# Role
* Alguém que pode receber a permissão.

# Polices
* Documento que da a permissão
* Polices de identidade: 
	* Polices Gerenciadas: Criadas pela AWS
	* Polices Não Gerencias: Você cria e você mantem.
* Police de Recurso:
	* Entra no recurso(S3, Lambda, etc..) e adiciona uma politica para o recurso. Utilizado para dar permissões mais especificas, apenas para um bucket.
	* Necessário identificar qual é o usuário, UTILIZANDO O PRINCIPAL
Por padrão, sempre vão ter:
* Effect: Explicito se é Allow(Permitido) ou Deny(Negando)
* Action : Read, Write, Delete, etc..
	* Condition: Adiciona condições na Police. Ex: NotIPAddress: {192.0.2.0/24} A Regra só irá valer se não for o ip setado. Ou seja, irá bloquear se não for aquele IP.
* Resource : Permite dar permissão especifica, exemplo: Apenas uma pasta no Bucket, ou toda a Raiz
* Principal (APENAS PARA POLICES DE RECURSO): Se terá alguma permissão escpecifica.

# Hospedar um site no S3
1. Criar um bucket.
2. Subir o HTML
3. Deixar o publico com 
.... (Continuar)

# S3
* Armazenamento é feito em Blocos. (EBS - Elastic bloc Store)
* Sistema de arquivos blocados suportam edição no meio dos arquivos
* File Share: Troca de arquivos no servidor, semelhante a unidades de rede compartilhada. (EFS - Elastic file system)
* Armazenamento de objetos. (S3 - Simple Storage Service )
	* Tipo de armazenamento acessado pela internet, onde salva o binario do arquivo e os metadados(dados de dados)
	* Armazenamento de TAG's (Facilitando na pesquisa)
* Bucket Limite: Não possui limite
* Objeto Limite: 5TB de arquivo\Objeto.
* Todo objeto no S3, tem uma URL Global e única.
* URL: s3-<aws-region>.amazonaws.com/<bucket-name>/<object-key>
* Não existem "pastas", apenas pré-fixos.
