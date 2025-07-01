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
* Por padrão, vem como privado, mas pode virar publico.
* Pode utilizar Polices e Roles.
* Pode permitir usuário especificos do IAM
* Pode dar acesso "publico" para um objeto especifico, criando um URL publica temporaria, já com tempo para expirar.
* Uso da Região pode impactar no :
	* Custo
	* Latência
	* Questões legais
	* Disponibilidade de serviço
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
* Possuem 2 tipos de acesso: 
	* Quentes: Acesso a todo o momento (Mais caro)
	* Frios: Tem que trazer novamente o arquivo para poder acessar (Mais barato)
* Lifecycle: Definir qual o tempo que será guardado o arquivo.
	* Importante para diminuir os custos, sendo apagando o arquivo ou movendo o arquivo para outro tipo de acesso (um mais barato).
## Versionamento
* Cada versão é uma cópia INTEIRA do objeto, onde ele cria um código de versão diferente para cada versão gerada.
* Por padrão, o bucket é gerado com versionamento desligado.
* Uma vez ligado, não pode desabilitar. MAS... pode pausar.
* Ao apagar um objeto versionamento, é criado uma nova versão com ele "apagado".
* É possível voltar um objeto deletado, apagando a última versão que ele foi definido como "apagado"
* NÃO É POSSÍVEL EDITAR UM ARQUIVO NO S3
* É possível pegar uma versão especifica do arquivo, tendo o nome e id de versão

# CORS
* O que é? É quando um código de um site, tenta acessar o conteudo de outro site, mas esse outro site não permita que ele acesse.
* Para liberar o CORS, pode utilizar o xml abaixo onde possui identifadores de cabeçalhos, metodos, etc...
 [
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://127.0.0.1:5500"
        ],
        "ExposeHeaders": [
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3000
    }
]
* TODO O Bucket é criptografado por padrão.
* Server Side: A AWS salva o arquivo criptografado no disco e Ao baixar, descriptografa
* É possível o cliente fazer a criptografia, mas a AWS não se responsabiliza e a responsabilidade cai para a aplicação


------------------------------------
# Elastic Computer Cloud - EC2
* Segundo serviço da AWS - Serviço que roda computadores em nuvem
* Para armazenamento do HD do servidor, fica no Amazon Elastic Block Store (EBS)
* Intance store -> Armazenamento ephemeral -> É apagado assim que a maquina é deletada.

Manual de boas praticas
1. Utilizar o user data para update. Preferir utilizar o user data e evitar comendos manuais.

##AMI Deployment modeles
* Basic AMI: Configurações básicas
* Silver: Ajuste de configuração manualmente
* Golden:  Imagem que não precisa de alteração.

Placement Strategies
* CLuster
* Partition
* Spread

#Amazon EC2 purchase models
* On-Demand - Paga mais caro, mas pode ser acesso em qualquer horário, qualquer momento
* Reserved - Mais economico, reservar cm antecedencia informando quando vai user e o que vai ser usado.
	AURI - Pagamento adiantado cm 75% de deconto
	PURI - Paga metade adiantado e tem 50%  de desconto
	NURI - Pagamento todo o mês
* Savings Plans - Compromisso de gasto, firmar um acordo cm a AWS que será gasto $/hour.
	Terá um desconto aplicado em cima do gasto fixo.
	Possível fazer ajustes no servidor
* Amazon EC2 Spot - Leilão da AWS, Compra servidores que não estão em uso por um preço barato, porém caso a AWS queira usar, terá 2 minutos para liberar a maquina

* Segurity
	* Não dependa de intervenção manual para proteger as maquina. Utilize mecanismos automaticos
* Performance Efficenc
* Cost optimizatio:
	* Selecione corretamente o recurso tamanho e numero
	* Escolhe corretamente o plano
* Sustentabilidade
	* Escolha de forma conciente, sem disperdicios.

# Amazon RDS
* É um banco Relaciona

# Amazon DynamoDB
# Amazon Neptune
# Amazon ElastiCache


# REDES AWS
* AWS VPC -
  * Ajusta o tamanho da sua rede;
  ## Sub-net
  * É possível criar Sub-nets, onde uma não pode falar com outra, mesmo que esteja na mesma VPC.
  * Subnets estão dentro de uma AZ.
  * Sub-net Privada: Os recursos tendo dela, estão disponiveis de dentro para fora e de fora para dentro. 
  * Sub-net Publica: Possíbilita a Configuração de uma VPC para acesso publico.
    * Internet Gateway: Ponta de entrada da VPC.
    * Tabela de Rotas: Em uma tabela de rotas, precisa  ter um regra de saida para o internet gateway. (A regra de saida que torna ele publica)
    * O serviço que está dentro da rede publica, tem que ter um IP Publico.

* Níveis de Isolamentos:
  1. Conta da AWS: Um cliente só pode acessar o que está na propria conta. 
  2. Regiões: O que está dentro de uma região, não pode conversar com outra região. (A não ser que seja configurado para tal.)
    2.1 Toda a vez que for criada uma rede, a rede será daquela região.
  3. Toda a VPC é interconectada. Basicamente, se tenho 3 servidor em az's diferentes, a VPC faz com que a velocidade seja igual como se tivesse um cabo de rede conectado.
  ## Tabela de Rotas:
  * É um serviço que diz para o dispositivo para onde ele irá enviar o pacote.
  * Toda a VPC tem uma tabela de rotas padrão, onde vem por padrão que o CDIR VPC -> CDIR VPC (Qualquer aparelho na VPC pode falar com qualquer aparelho na VPC)
  
  ## DHCP: Protocologo de distribuição de IP's

  ## Netwirk ACL (NACL)
  * É um firewall statless (não lembra de você, tem que ter autorização de entrada e saida)
  
  ## Security Group
  * Precisa de permissão apenas para entrada, para saida ele já autoriza.

* Uma alternativa para acessar a internet em computadores que não tem acesso são o Jump box e o bastion hosts.
* 

## Interface VPC Endpoinbt
* Possibilita fazer um tunel de VPN para conectar na AWS s3 por exemplo, entre outros 200serviços.

## Gateway VPC endpoint
* POssibilita conectar também em serviços internos, porém apenas para S3 e DynamoDB mas gratuito, com banda ilimitada e redundante

## Gateway Load ballancing
* Fica exposto para a internet e distribui a carga para as maquinas que são privadas e não tem acesso a internet

## AWS Transit Gateway
* É um gerenciador central que conecta as VPC's.
* É um serviço Regional.
* Gerencia até 5k attachments: Ex: Redes, VPN,
* Para cronectar dois Transit Gateway de duas regiões é possível utilizar um Transit Gateway Peering


## AWS Direct Connect
* É uma rede dedicata que liga uma AZ a uma empresa.
* Possível chegar até 100GB
* Por padrão, os dados são trafegados sem criptografia, porém é possível adicionar uma VPN criptografando.
* 

## Aula 19/05
## VPC Peering
* Problema que ele resolve: Necessidade de comunicação privada entre duas VPCs na AWS (mesmo ou diferentes contas/regiões)
* Permite que instâncias em VPCs diferentes se comuniquem como se estivessem na mesma rede
* Não suporta transitividade (VPC A ↔ B e B ↔ C não implica A ↔ C)
* Tráfego é roteado internamente pela rede da AWS, sem uso da internet

## AWS VPN Sito-to-site
* Problema que ele resolve: Conectar uma rede local (on-premises) a uma VPC na AWS com segurança
* Usa IPsec para criar túneis criptografados entre os ambientes
* É necessário um Customer Gateway (CGW) e um Virtual Private Gateway (VGW)
* Pode ser redundante com dois túneis ativos para alta disponibilidade
## AWS Direct Connect
* Problema que ele resolve: Latência e largura de banda limitadas ao usar conexão pela internet
* Conexão de rede dedicada entre a infraestrutura local e a AWS
* Mais estável, com menor latência e sem passar pela internet pública
* Ideal para grandes volumes de dados e necessidades críticas de desempenho

## AWS Cognito
* Problema: Em um sistema com vários usuários, acaba sendo inviavel fazer essa associação permissão x usuário
* Para isso, é utilizado o IAM Groups.
* Grupos só podem ter usuário e permissões.
* Com o cognito, é possível gerar chaves JWT para sua aplicação realizar authenticação no Cognito
* 50.000 usuários gratuitos

### AWS Cognito USer Pool
* Possibilita trocar imagens de login
* Possibilita Autenticação de 2 fatores

## Role Base
* Criação de Roles é feita para que um usuário tenha acesso temporário a um determinado serviço.
* Mesmo após criar a Role e atribuir, a permissão só será aplicado caso o usuário acesse a URL.
* ARN = Amazon Resource Name

## ABAC - Atribut Basic Access Controll
* Na police, é utilizado para validação de quem pode utilizar a police ou não pela condition da police

## AWS Organization
* Permite gerenciar uma hieraquia de contas, possíbilitando ver os valores de todas as contas em um só lugar
* Possibilita ter mais desconto quanto mais usa.
* Como fazer:
1. Escolha uma conta para virar a Root;
2. A Conta Root, pode disparar uma invite para as demais contas se juntarem a organização.
3. Ao aceitar, as demais contas ficam dependendo de algumas permissoes da root.
4. A partir disso, pode ser habilitado 
* SCP Policy - Politica de governamento na AWS. Limita o que o usuário pode fazer. Ex: Não pode criar instancias s3 no brasil
  * Grant:  Da permissao
    * Identidade 
    * Recurso
  * Limit: Limita a Permissão 
    * SCP
    * Permition Boundary 

# Criptografia
## Criptografia Simetrica
* Uma chave criptografa e descriptografa os dados

## Criptografia Assimetrica
* Uma chave para criptografar outra chave para a chave descriptografar;

## AWS KMS - 
* Cofre de senhas da AWS que guarda todas as chaves criptografadas;

# AWS WAF
* É um firewall dinamico que que consegue capturar tipos de ataque como: SQL Injection, Javascript
* É possível criar regras personalizadas. Como: Todos os usuário fora do Brasil não vão conseguir enviar pacotes.

# AWS Macie
* É uma ferramante que consegue encontrar dados sensiveis no seu armazenamento. EX: Localizar CPF's em buckets do s3

# AWS Inspector
* Procura vunerabilidade conhecidas no seu ambiente e lhe avisa.
* Scanneia: EC2

# AWS Detective
* Identifica comportamentos estranhos na sua conta.

# AWS Security Hub
* Painel de controle de segurança geral
* AWS Macie, Inspector, etc..


# Monitoramento
## Por que Implementar?
1. Verificar a saúde da operação, se está rodando como deveria
2. Utilização do Servidor: Verificar se pode diminuir ou se é necessário aumentar o servidor
3. Performance: Caso o cliente reclame de lentidão, pode ser por conta da aplicação ou servidor, esse monitoramento irá ajudar a descobrir onde está a lentidão
4. Segurança: Em caso de ataques, é normal o processamento aumentar e com o monitoramento é possível ver isso.

## CloudWatch
* Monitora LOG - São pagos
* Monitora Métricas: CPU, Mémoria - AWS fornece gratuito
* É possível gerar Gráficos;
* É possível gerar alarmes;
* Ao ser gerado um log, por padrão, ele cria para nunca excluir. Alterar para apagar de x em x tempo

## Event Bridge
* Monitoramento da AWS em tempo real.
* Event Bus: Eventos da que a AWS Gera e a aplicação pode consumir o evento

# Amazon EC2
* Agendamento de Ações.
  Exemplo: Subir servidores com base no agendamento
* Predictive policy: É uma IA que vai gerenciar os EC2 e verifica quando precisa subir mais ou não.

# Load Balance
* Problema: Distribuição desigual de tráfego entre instâncias pode causar sobrecarga e falhas
* Para isso, é utilizado o Elastic Load Balancer (ELB)
* Distribui automaticamente o tráfego entre múltiplas instâncias em uma ou mais zonas de disponibilidade
* Existem três tipos principais: Application (HTTP/HTTPS), Network (TCP/UDP), e Gateway (para tráfego IP)
* Suporte a health checks para garantir que apenas instâncias saudáveis recebam tráfego

# DNS
* Problema: Dificuldade de lembrar e gerenciar endereços IP de servidores e serviços
* Para isso, é utilizado o serviço de DNS (como o Amazon Route 53)
* Converte nomes de domínio (ex: www.exemplo.com) em endereços IP
* Suporte a balanceamento de carga com registros do tipo "Alias" * integrados a ELB, S3, e outros
* Pode ser usado para failover, roteamento baseado em geolocalização e * latência
* Amazon Route 53: serviço de DNS gerenciado da AWS que também oferece * registro de domínios e checagens de saúde; altamente disponível e * escalável

# CloudFormation utilizando yaml
* Problema: Criar e gerenciar recursos AWS manualmente é demorado e propenso a erros
* Para isso, é utilizado o AWS CloudFormation com arquivos de template o (template.yaml)
  * O template.yaml define a infraestrutura como código (IaC) — descreve recursos como funções Lambda, APIs, bancos de dados, etc.
* Escrita no formato YAML (ou JSON), com seções como:
  * AWSTemplateFormatVersion: versão do template
  * Resources: onde os recursos são definidos (ex: S3, Lambda, DynamoDB)
  * Parameters: permite passar valores externos para o template
  * Outputs: retorna informações úteis ao final da criação (ex: ARN de um recurso)
* Usado com ferramentas como o AWS SAM (Serverless Application Model), que facilita o deploy de aplicações serverless
* Exemplo de uso com sam deploy, que converte o template em uma stack no CloudFormation e cria os recursos definidos

# Arquitetura desacoplada
* Problema: Normalmente as aplicações só tem uma camada, onde se cair o banco de dados, já interrompe toda a aplicação.
* Como resolver: 
1. Podemos utilizar Aplication LoadBalancer(HTTP) para controlar as requisições e direcionar para Intancias disponiveis.
2. Utilizar Network Loadbalance para controlar as requisições ao banco de dados. (TCP/UDP)
3. Quebrando a aplicação em módulos e migrar para microserviços
4. Utilizar SQS e SNS para implementação de filas nas requisições.

# Amazon SQS (Simple Queue Service)
* Problema: Sistemas desacoplados precisam se comunicar de forma assíncrona e confiável
* Serviço de fila gerenciado que armazena mensagens até que sejam processadas por outro serviço
* Garante que mensagens não sejam perdidas, mesmo se o consumidor estiver temporariamente offline
* Pode ser padrão (alta taxa de throughput, entrega eventual) ou FIFO (ordem garantida e sem duplicidade)
* Exemplo: uma aplicação envia pedidos para a fila, e um worker processa essas mensagens em segundo plano

# Amazon SNS(Simple Notification Service)
* Problema: Notificar múltiplos sistemas ou usuários de forma rápida e * escalável
* Serviço de publicação/assinatura (pub/sub) para envio de mensagens a * múltiplos destinos
* Destinos podem ser: email, SMS, Lambda, SQS, ou HTTP endpoints
* Baixa latência e altamente escalável