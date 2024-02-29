{
  "cdps": {
    "CDPS": {"feign": [], "bootstrap": [], "application": {}},
    "cdps-perfil-pj-web-angular": {"feign": [], "bootstrap": [], "application": {}},
    "cdps-bens-cadastrados-java": {
      "feign": [],
      "bootstrap": [
        {
          "integrations": "acpf-integration;mcsv-integration;atcl-integration;cnio-corp; ctas-integration; ctcr-integration; original-legacy; cdps-corp"
        }
      ],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-consulta-listas-restritivas-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-tratamento-cep-java": {
      "feign": [{"file": "FindCep.java", "url": "cep.request.url"}],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "cep.request.url",
            "url_text": "vshacad.bcocorporate.ad:5052/api/Endereco/v1/ObterEndereco",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "cep.request.url",
            "url_text": "vshacad.bcocorporate.ad:5052/api/Endereco/v1/ObterEndereco",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "cep.request.url",
            "url_text": "vsacadprdback:5052/api/Endereco/v1/ObterEndereco",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-dados-reduzidos-cliente-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-manutencao-prospect-java": {
      "feign": [{"file": "AcadFeign.java", "url": "acad.java.url"}],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.java.url",
            "url_text": "vshacad.bcocorporate.ad:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.java.url",
            "url_text": "vshacad.bcocorporate.ad:5052",
          }
        ],
        "application-prd.properties": [
          {"variable_name": "acad.java.url", "url_text": "vsacadprdback:5052"}
        ],
        "application.properties": [],
      },
    },
    "cdps-consultar-informacoes-empresas-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-agente-assistente-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-consultar-informacoes-cliente-mint-java": {
      "feign": [],
      "bootstrap": [
        {"integrations": "cdps-corp; original-legacy; cdps-integration"}
      ],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-consulta-grupos-relacionamento-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-coding-dojo-java": {"feign": [], "bootstrap": [], "application": {}},
    "cdps-cadastro-dados-minimos-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-pendencias-clientes-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy\n"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-consultar-informacoes-cliente-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-atualizacao-dados-cadastrais-java": {
      "feign": [],
      "bootstrap": [
        {
          "integrations": "cdps-corp; cdps-integration; original-legacy; acad-integration\n"
        }
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "bcodacadapp01:5052",
          },
          {
            "variable_name": "acad.consultas.dominios.java.url",
            "url_text": "acad-consultas-dominios-java.apps.ocp-h.original.com.br",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "vshacad.bcocorporate.ad:5052",
          },
          {
            "variable_name": "acad.consultas.dominios.java.url",
            "url_text": "acad-consultas-dominios-java.apps.ocp-h.original.com.br",
          },
        ],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-orq-cadastro-nao-correntista-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "bcodacadapp01:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "bcodmswrkctn01:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc-dev.svc.cluster.local:8080/v1/customers/partnerships",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.apps.ocp-d.original.com.br/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.acadMininumDataUrl",
            "url_text": "bcodacadapp01:5052/api/PessoaFisica/v1/SalvarPessoaFisicaParceria",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "vshacad.bcocorporate.ad:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "vshmsctnprodutos:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc-hml.svc.cluster.local:8080/v1/customers/partnerships",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.apps.ocp-h.original.com.br/",
          },
          {
            "variable_name": "original.register.acadMininumDataUrl",
            "url_text": "vshacad.bcocorporate.ad:5052/api/PessoaFisica/v1/SalvarPessoaFisicaParceria",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "vsacadprdback:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "vsmsctnprodutos:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc.svc.cluster.local:8080/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.acadMininumDataUrl",
            "url_text": "vsacadprdback:5052/api/PessoaFisica/v1/SalvarPessoaFisicaParceria",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-documentos-nao-correntista-java": {
      "feign": [],
      "bootstrap": [{"integrations": "gedc-integration"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-orq-dados-cadastrais-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-integration; parc-integration"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-dados-cadastrais-nao-correntista-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-contas-clientes-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy\n"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-incremental-diario-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-consultar-informacoes-cliente-pix-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-officer-java-ocp": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          }
        ],
      },
    },
    "cdps-officer-java-ocp-old": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          }
        ],
      },
    },
    "cdps-dados-cadastrais-desatualizados-pu-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-dados-cadastrais-pu-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-informacoes-cadastrais-operacoes-atraso-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-extrair-massa-clientes-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-pessoa-juridica-java": {
      "feign": [],
      "bootstrap": [
        {"integrations": "cdps-corp; cdps-integration; original-legacy"}
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "microsservice.acad.server",
            "url_text": "bcohacadapp01:5052",
          },
          {
            "variable_name": "microsservice.parse.base-path",
            "url_text": "vsmscorporativo11:8164/cdps/acad-parse/v1/",
          },
          {
            "variable_name": "microsservice.cdps-atualizacao.server",
            "url_text": "cdps-atualizacao-dados-cadastrais-java.apps.ocp-d.original.com.br",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "microsservice.acad.server",
            "url_text": "bcohacadapp01:5052",
          },
          {
            "variable_name": "microsservice.parse.base-path",
            "url_text": "vsmscorporativo11:8164/cdps/acad-parse/v1/",
          },
          {
            "variable_name": "microsservice.cdps-atualizacao.server",
            "url_text": "cdps-atualizacao-dados-cadastrais-java.apps.ocp-h.original.com.br",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "microsservice.acad.server",
            "url_text": "bcopacadapp01:5052",
          },
          {
            "variable_name": "microsservice.parse.base-path",
            "url_text": "vsmscorporativo11:8164/cdps/acad-parse/v1/",
          },
          {
            "variable_name": "microsservice.cdps-atualizacao.server",
            "url_text": "cdps-atualizacao-dados-cadastrais-java.original.com.br",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-arquivo-dados-clientes-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-encerrar-contas-irregulares-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-atualizar-status-documento-batch-java": {
      "feign": [],
      "bootstrap": [{"integrations": "original-legacy; cdps-corp; fwcl-corp"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-verifica-dados-irregulares-batch-java": {
      "feign": [],
      "bootstrap": [{"integrations": "original-legacy; cdps-corp; fwcl-corp"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-atualizar-dados-empregador-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.empregador.net",
            "url_text": "bcodacadapp01:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.empregador.net",
            "url_text": "bcohacadapp01:5052",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.empregador.net",
            "url_text": "vsacadprdback:5052",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-atualizar-dados-conjuge-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.conjuge.net",
            "url_text": "bcodacadapp01:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.conjuge.net",
            "url_text": "bcohacadapp01:5052",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.url.cdps.atualizar.dados.conjuge.net",
            "url_text": "vsacadprdback:5052",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-pendencia-dados-cliente-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-atualizar-contato-cadastro-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "microsservice.acad-apoio-cadastro.base-path",
            "url_text": "bcodacadapp01:5052/api",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "microsservice.acad-apoio-cadastro.base-path",
            "url_text": "bcohacadapp01:5052/api",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "microsservice.acad-apoio-cadastro.base-path",
            "url_text": "bcopacadapp01:5052/api",
          }
        ],
        "application.properties": [
          {
            "variable_name": "microsservice.acad-apoio-cadastro.base-path",
            "url_text": "bcodacadapp01:5052/api",
          }
        ],
      },
    },
    "cdps-prospect-corporate-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-complementar-informacoes-cliente-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-campanhas-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "service.acade.url",
            "url_text": "bcodacadapp01:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "service.acade.url",
            "url_text": "bcohacadapp01:5052",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "service.acade.url",
            "url_text": "bcopacadapp01:5052",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-validacao-conta-raiz-cnpj-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-rendas-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.salvar.renda.api.url",
            "url_text": "bcodacadapp01:5052/api/PessoaFisica/v1/AtualizarRenda",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.salvar.renda.api.url",
            "url_text": "bcohacadapp01:5052/api/PessoaFisica/v1/AtualizarRenda",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "acad.salvar.renda.api.url",
            "url_text": "vsacadprdback:5052/api/PessoaFisica/v1/AtualizarRenda",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-dominios-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-officer-java": {
      "feign": [
        {
          "file": "CustomerAcadFeignService.java",
          "url": "acad.apoio.cadastro.url",
        }
      ],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "vshacad.bcocorporate.ad:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "vshacad.bcocorporate.ad:5052",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "vsacadprdback:5052",
          }
        ],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          }
        ],
      },
    },
    "cdps-empresas-java": {
      "feign": [
        {
          "file": "AcadDomainClient.java",
          "url": "acad.consultas.dominios.java.url",
        },
        {
          "file": "AcadRegistrationAccountName.java",
          "url": "acad.apoio.cadastro.url",
        },
        {
          "file": "AcadRegistrationSuport.java",
          "url": "acad.apoio.cadastro.url",
        },
        {
          "file": "CdpsDataValidation.java",
          "url": "cdps.validacao.dados.java.url",
        },
        {
          "file": "CdpsSearchClientInfos.java",
          "url": "cdps.consultar.informacoes.cliente.java.url",
        },
      ],
      "bootstrap": [
        {
          "integrations": "cdps-corp; original-legacy; cdps-integration; acad-integration"
        }
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "bcohacadapp01:5052",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.apoio.cadastro.url",
            "url_text": "bcohacadapp01:5052",
          }
        ],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-pendencias-java": {"feign": [], "bootstrap": [], "application": {}},
    "cdps-carga-pendencias-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-desativacao-campanhas-vencidas-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-extrair-dados-cliente-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application.properties": [],
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
      },
    },
    "cdps-consultas-id-fisico-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "swagger.api.license.url",
            "url_text": "www.apache.org/licenses/LICENSE-2.0.html",
          },
        ],
      },
    },
    "cdps-enriquecedor-transacoes-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-verificar-cliente-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br/politicaprivacidade/",
          },
          {
            "variable_name": "swagger.api.licenceUrl",
            "url_text": "www.apache.org/licenses/LICENSE-2.0.html",
          },
        ],
      },
    },
    "cdps-produtos-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          }
        ],
      },
    },
    "cdps-validacao-posse-dados-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.validation.atadUrl",
            "url_text": "bcodmswrkctn01:8694/atad-validacao-posse-dados-java/v1/data-possessions",
          },
          {
            "variable_name": "original.validation.sendMessageUrl",
            "url_text": "bcohmswrk11:8250/cmmo-ceno/v1/processNotification",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.validation.atadUrl",
            "url_text": "bcohmswrkctn01:8694/atad-validacao-posse-dados-java/v1/data-possessions",
          },
          {
            "variable_name": "original.validation.sendMessageUrl",
            "url_text": "bcohmswrk11:8250/cmmo-ceno/v1/processNotification",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.validation.atadUrl",
            "url_text": "vsmsctnprodutos:8694/atad-validacao-posse-dados-java/v1/data-possessions",
          },
          {
            "variable_name": "original.validation.sendMessageUrl",
            "url_text": "vsmscorporativo11:8250/cmmo-ceno/v1/processNotification",
          },
        ],
        "application.properties": [
          {
            "variable_name": "original.swagger.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "original.swagger.contactUrl",
            "url_text": "www.original.com.br",
          },
        ],
      },
    },
    "cdps-sincronizacao-tabelas-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "swagger.api.license.url",
            "url_text": "www.apache.org/licenses/LICENSE-2.0.html",
          },
        ],
      },
    },
    "cdps-orq-abertura-cadastro-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "bcodacadapp01:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "bcodmswrkctn01:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc-dev.svc.cluster.local:8080/v1/customers/partnerships",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.apps.ocp-d.original.com.br/v1/customers/partnerships",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "vshacad.bcocorporate.ad:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "vshmsctnprodutos:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc-hml.svc.cluster.local:8080/v1/customers/partnerships",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.apps.ocp-h.original.com.br/",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.register.acadUrl",
            "url_text": "vsacadprdback:5052/api/PessoaFisica/v1/IncluirPessoaFisica",
          },
          {
            "variable_name": "#original.register.partnershipUrl",
            "url_text": "vsmsctnprodutos:8086/parc-abertura-cadastro-java/v1/customers/partnerships",
          },
          {
            "variable_name": "original.register.partnershipUrl",
            "url_text": "parc-abertura-cadastro-java.parc.svc.cluster.local:8080/v1/customers/partnerships",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-batimento-grupos-restricoes-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-enriquecer-dados-tef-parcerias-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "swagger.api.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "swagger.api.license.url",
            "url_text": "www.apache.org/licenses/LICENSE-2.0.html",
          },
        ],
      },
    },
    "cdps-vinculo-operacoes-clientes-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-cmm-rest-java": {
      "feign": [
        {
          "file": "CustomerRestService.java",
          "url": "original.url.rest.prospect.suppliers",
        },
        {
          "file": "KycRestService.java",
          "url": "original.url.rest.visit-report-kyc.base",
        },
        {
          "file": "ProspectAcadServiceFeign.java",
          "url": "original.acad.consulta.url",
        },
      ],
      "bootstrap": [
        {
          "integrations": "acpf-integration;mcsv-integration;atcl-integration;cnio-corp;cdps-integration;original-legacy\n\n"
        }
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.url.rest.prospect.suppliers",
            "url_text": "vshmsctnprodutos:8119/reip/prospect-suppliers-status-pj",
          },
          {
            "variable_name": "original.url.rest.visit-report-kyc.base",
            "url_text": "vshmsctnprodutos:8275/cdps-atualizar-cadastro-java",
          },
          {
            "variable_name": "original.acad.acesso.url",
            "url_text": "bcodacadapp01.bcocorporate.ad:5054/AcessoService.svc",
          },
          {
            "variable_name": "original.acad.consulta.url",
            "url_text": "bcodacadapp01.bcocorporate.ad:5051/",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.url.rest.prospect.suppliers",
            "url_text": "vshmsctnprodutos:8119/reip/prospect-suppliers-status-pj",
          },
          {
            "variable_name": "original.url.rest.visit-report-kyc.base",
            "url_text": "vshmsctnprodutos:8275/cdps-atualizar-cadastro-java",
          },
          {
            "variable_name": "original.acad.acesso.url",
            "url_text": "bcohacadapp01.bcocorporate.ad:5054/AcessoService.svc",
          },
          {
            "variable_name": "original.acad.consulta.url",
            "url_text": "bcohacadapp01.bcocorporate.ad:5051/",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.url.rest.prospect.suppliers",
            "url_text": "vsmsctnprodutos:8119/reip/prospect-suppliers-status-pj",
          },
          {
            "variable_name": "original.url.rest.visit-report-kyc.base",
            "url_text": "vsmsctnprodutos:8275/cdps-atualizar-cadastro-java",
          },
          {
            "variable_name": "original.acad.acesso.url",
            "url_text": "bcopacadapp01.bcocorporate.ad:5054/AcessoService.svc",
          },
          {
            "variable_name": "original.acad.consulta.url",
            "url_text": "bcopacadapp01.bcocorporate.ad:5051/",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-segmentos-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [
          {
            "variable_name": "br.com.original.swagger.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "br.com.original.swagger.contact.url",
            "url_text": "www.original.com.br",
          },
        ],
      },
    },
    "cdps-operacoes-clientes-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.endpoint.system.user",
            "url_text": "tbgr-usuario-sistema-java.tbgr-dev.svc.cluster.local:8080",
          },
          {
            "variable_name": "original.endpoint.status",
            "url_text": "tbgr-consultas-java.tbgr-dev.svc.cluster.local:8080",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.endpoint.system.user",
            "url_text": "tbgr-usuario-sistema-java.tbgr-hml.svc.cluster.local:8080",
          },
          {
            "variable_name": "original.endpoint.status",
            "url_text": "tbgr-consultas-java.tbgr-hml.svc.cluster.local:8080",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.endpoint.system.user",
            "url_text": "tbgr-usuario-sistema-java.tbgr.svc.cluster.local:8080",
          },
          {
            "variable_name": "original.endpoint.status",
            "url_text": "tbgr-consultas-java.tbgr.svc.cluster.local:8080",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-vinculo-operacoes-relacionadas-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-cadastro-pep-fatca-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-vinculo-operacoes-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-servicos-cmm-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "cmm.endpoint",
            "url_text": "VSCMMHOM:7080/CMM_SERVICES",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "cmm.endpoint",
            "url_text": "VSCMMHOM:7080/CMM_SERVICES",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "cmm.endpoint",
            "url_text": "VSCMMPROD:7080/CMM_SERVICES",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-retentativa-cadastro-parceiro-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-pesquisar-dados-descaracterizacao-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application.properties": [],
      },
    },
    "cdps-obter-clientes-novos-atualizados-onu-batch-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy; fwcl-corp"}],
      "application": {
        "application.properties": [],
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
      },
    },
    "cdps-mascarar-dados-descaracterizacao-oracle-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application.properties": [],
      },
    },
    "cdps-mascarar-dados-descaracterizacao-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application.properties": [],
      },
    },
    "cdps-listas-restritivas-batch-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy; fwcl-corp"}],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-encerramento-conta-pj-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-extrair-dados-descaracterizacao-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application.properties": [],
      },
    },
    "cdps-informacoes-cadastrais-interface-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-contas-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "cmm.endpoint",
            "url_text": "bcodcmm01:7080/CMM_SERVICES",
          }
        ],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-contas-2025-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-carga-cep-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-abertura-cadastro-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy\n"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "cmm.client.endpoint",
            "url_text": "BCODCMM01:7080/CMM_SERVICES",
          },
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "bcodacadapp01:5051/CyberbankService.svc?wsdl",
          },
          {
            "variable_name": "url.partnership",
            "url_text": "bcodmswrkctn01:8086/parc/partnership-registry/v1/",
          },
          {
            "variable_name": "cep.uri",
            "url_text": "bcodacadapp01:5055/EnderecoService.svc",
          },
          {
            "variable_name": "acesso.uri",
            "url_text": "bcodacadapp01:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.incluir.pessoa.fisica",
            "url_text": "bcodacadapp01:5052/api/PessoaFisica/v1/Salvar",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "cmm.client.endpoint",
            "url_text": "VSCMMHOM:7080/CMM_SERVICES",
          },
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "BCOHACADAPP01:5051/CyberbankService.svc",
          },
          {
            "variable_name": "url.partnership",
            "url_text": "bcohmetaapp01:8086/parc/partnership-registry/v1/",
          },
          {
            "variable_name": "cep.uri",
            "url_text": "bcohacadapp01:5055/EnderecoService.svc",
          },
          {
            "variable_name": "acesso.uri",
            "url_text": "bcohacadapp01:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.incluir.pessoa.fisica",
            "url_text": "bcohacadapp01:5052/api/PessoaFisica/v1/Salvar",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "cmm.client.endpoint",
            "url_text": "VSCMMPROD:7080/CMM_SERVICES",
          },
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "VSACADPRDBACK:5051/CyberbankService.svc",
          },
          {
            "variable_name": "url.partnership",
            "url_text": "vsmscorporativo8:8086/parc/partnership-registry/v1/",
          },
          {
            "variable_name": "cep.uri",
            "url_text": "VSACADPRDBACK:5055/EnderecoService.svc",
          },
          {
            "variable_name": "acesso.uri",
            "url_text": "VSACADPRDBACK:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.incluir.pessoa.fisica",
            "url_text": "vsacadprdback.bcocorporate.ad:5052/api/PessoaFisica/v1/Salvar",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-atualizar-cadastro-java": {
      "feign": [
        {
          "file": "FindSolicitarCartaoClient.java",
          "url": "url.servico.solicitarCartao",
        }
      ],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "cyber.bank.url",
            "url_text": "bcodacadapp01:5051/CyberbankService.svc",
          },
          {
            "variable_name": "pessoa.fisica.url",
            "url_text": "bcodacadapp01:5051/PessoaFisicaService.svc",
          },
          {
            "variable_name": "acesso.service.url",
            "url_text": "bcodacadapp01:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.atualizar.cadastro",
            "url_text": "bcodmswrk01:8275",
          },
          {
            "variable_name": "#atualizar.cadastro.endpoint",
            "url_text": "bcodmswrk01:8275/cdps-atualizar-cadastro-java/v1",
          },
          {
            "variable_name": "atualizar.cadastro.endpoint",
            "url_text": "localhost:8080/cdps-atualizar-cadastro-java/v1/swagger-ui.html#",
          },
          {
            "variable_name": "cmm.endpoint",
            "url_text": "bcoacmm01:7080/CMM_SERVICES",
          },
          {
            "variable_name": "url.embossing.name",
            "url_text": "bcodmswrkctn01:8275/cdps-atualizar-cadastro-java/v1/embossed-name/",
          },
          {
            "variable_name": "url.servico.solicitarCartao",
            "url_text": "bcodacadapp01:5052/",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "cyber.bank.url",
            "url_text": "bcohacadapp01:5051/CyberbankService.svc",
          },
          {
            "variable_name": "pessoa.fisica.url",
            "url_text": "bcohacadapp01:5051/PessoaFisicaService.svc",
          },
          {
            "variable_name": "acesso.service.url",
            "url_text": "bcohacadapp01:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.atualizar.cadastro",
            "url_text": "bcodmswrk01:8275",
          },
          {
            "variable_name": "atualizar.cadastro.endpoint",
            "url_text": "bcodmswrk01:8275/cdps-atualizar-cadastro-java/v1",
          },
          {
            "variable_name": "url.embossing.name",
            "url_text": "vshmsctnprodutos:8275/cdps-atualizar-cadastro-java/v1/embossed-name/",
          },
          {
            "variable_name": "url.servico.solicitarCartao",
            "url_text": "bcohacadapp01:5052/",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "cyber.bank.url",
            "url_text": "bcopacadapp01:5051/CyberbankService.svc",
          },
          {
            "variable_name": "pessoa.fisica.url",
            "url_text": "bcopacadapp01:5051/PessoaFisicaService.svc",
          },
          {
            "variable_name": "acesso.service.url",
            "url_text": "bcopacadapp01:5054/AcessoService.svc",
          },
          {
            "variable_name": "url.atualizar.cadastro",
            "url_text": "vsmsctnprodutos:8275",
          },
          {
            "variable_name": "atualizar.cadastro.endpoint",
            "url_text": "vsmsctnprodutos:8275/cdps-atualizar-cadastro-java/v1",
          },
          {
            "variable_name": "url.embossing.name",
            "url_text": "vsmsctnprodutos:8275/cdps-atualizar-cadastro-java/v1/embossed-name/",
          },
          {
            "variable_name": "url.servico.solicitarCartao",
            "url_text": "bcopacadapp01:5052/",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-campanhas-cliente-web-angular": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "parc.abertura.cadastro.endpoint",
            "url_text": "localhost:8125/camp/v1/",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "parc.abertura.cadastro.endpoint",
            "url_text": "localhost:8125/camp/v1/",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "parc.abertura.cadastro.endpoint",
            "url_text": "localhost:8125/camp/v1/",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-obter-nome-fonetica-lib-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [],
        "application-hml.properties": [],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "cdps-calculo-segmento-lib": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "#url.atualizar.cadastro",
            "url_text": "bcodmswrk01:8275",
          },
          {
            "variable_name": "#atualizar.cadastro.endpoint",
            "url_text": "bcodmswrk01:8275/cdps-atualizar-cadastro-java/v1",
          },
          {
            "variable_name": "#atualizar.cadastro.endpoint",
            "url_text": "localhost:8080/cdps-atualizar-cadastro-java/v1/swagger-ui.html#",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "url.atualizar.cadastro",
            "url_text": "bcodmswrk01:8275",
          },
          {
            "variable_name": "atualizar.cadastro.endpoint",
            "url_text": "bcodmswrk01:8275/cdps-atualizar-cadastro-java/v1",
          },
        ],
        "application-prd.properties": [],
        "application.properties": [],
      },
    },
    "ctad-ad-core-cdps-cadastropessoa": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "cdps-consultar-informacoes-cliente-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "br.com.original.swagger.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "br.com.original.swagger.contact.url",
            "url_text": "www.original.com.br",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "br.com.original.swagger.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "br.com.original.swagger.contact.url",
            "url_text": "www.original.com.br",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "br.com.original.swagger.termsOfServiceUrl",
            "url_text": "www.original.com.br",
          },
          {
            "variable_name": "br.com.original.swagger.contact.url",
            "url_text": "www.original.com.br",
          },
        ],
        "application.properties": [],
      },
    },
    "cdps-validacao-dados-java": {
      "feign": [],
      "bootstrap": [{"integrations": "cdps-corp; original-legacy"}],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "bcodacadapp01:5055/DominioService.svc",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "bcohacadapp01:5055/DominioService.svc",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "acad.client.endpoint",
            "url_text": "bcopacadapp01:5055/DominioService.svc",
          }
        ],
        "application.properties": [],
      },
    },
    "cdps-poderes-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "fepweb.endpoint",
            "url_text": "bcodfpwapl01:8080/fepwebws/services/CORE_CoreManagement_v5",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "fepweb.endpoint",
            "url_text": "bcohfpwapl01:8080/fepwebws/services/CORE_CoreManagement_v5",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "fepweb.endpoint",
            "url_text": "10.150.100.145:8080/fepwebws/services/CORE_CoreManagement_v5",
          }
        ],
        "application.properties": [],
      },
    },
  }
}
