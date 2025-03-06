# das-1-2025
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

