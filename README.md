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


-----
Aula (20/03/2025)
-----

