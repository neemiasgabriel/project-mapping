{
  "conv": {
    "mcsv-converter-informacoes-cliente-java": {
      "feign": [
        {
          "file": "CustomerDataConsumerFeign.java",
          "url": "cdps.consultar.informacoes.cliente.java.url",
        },
        {
          "file": "CustomerOperationsConsumerFeign.java",
          "url": "cdps.operacoes.clientes.java.url",
        },
        {
          "file": "SublimitsCustomerConsumerFeign.java",
          "url": "glpf.consulta.limites.java.url",
        },
      ],
      "bootstrap": [
        {
          "integrations": "mcsv-integration; ctcr-integration; cdps-integration; glpf-integration"
        }
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "original.url.rest.document",
            "url_text": "vshmsctnprodutos:8101/cmmo-gedc",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "original.url.rest.document",
            "url_text": "vshmsctnprodutos:8101/cmmo-gedc",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "original.url.rest.document",
            "url_text": "vsmsctnprodutos:8101/cmmo-gedc",
          }
        ],
        "application.properties": [],
      },
    },
    "utilitario-conversor-ansi-to-utf8": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
    "mcsv-convenio-guarda-chuva-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "url.cdps.customer.path",
            "url_text": "cdps-consultar-informacoes-cliente-java.apps.ocp-d.original.com.br/v1",
          },
          {
            "variable_name": "url.gagc.product-endpoint",
            "url_text": "bcodmswrkctn01:8589/gagc-garantias-imoveis-java/v1/products",
          },
          {
            "variable_name": "url.gagc.subproduct-endpoint",
            "url_text": "bcodmswrkctn01:8589/gagc-garantias-imoveis-java/v1/subproducts/",
          },
          {
            "variable_name": "url.ctas.status-endpoint",
            "url_text": "bcodmswrkctn01:8642/ctas-validacoes-java/v1/accounts/",
          },
          {
            "variable_name": "url.gagc.goods.endpoint",
            "url_text": "bcodmswrkctn01:8589/gagc-garantias-imoveis-java/v1/properties/warranties",
          },
          {
            "variable_name": "url.gagc.agreement.search",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements",
          },
          {
            "variable_name": "url.gagc.agreement.byid",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreement.status",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreementOperation",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreementsOperations/ ",
          },
          {
            "variable_name": "url.gagc.convenioguardachuva.inserirdadosconvenio.path",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.ged.pesquisar.obterdocumento",
            "url_text": "gedc-consultas-java.apps.ocp-d.original.com.br/v1/",
          },
          {
            "variable_name": "url.ged.inserir.documento",
            "url_text": "gedc-inclusao-manutencao-java.apps.ocp-d.original.com.br/v1/",
          },
          {
            "variable_name": "url.gagc.vincular.emprestimo.orq",
            "url_text": "bcodmswrkctn01:8706/gagc-orq-vinculacao-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.get.minutaria",
            "url_text": "bcodmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/",
          },
        ],
        "application-hml.properties": [
          {
            "variable_name": "url.cdps.customer.path",
            "url_text": "cdps-consultar-informacoes-cliente-java.apps.ocp-h.original.com.br/v1",
          },
          {
            "variable_name": "url.gagc.product-endpoint",
            "url_text": "bcohmswrkctn01:8589/gagc-garantias-imoveis-java/v1/products",
          },
          {
            "variable_name": "url.gagc.subproduct-endpoint",
            "url_text": "bcohmswrkctn01:8589/gagc-garantias-imoveis-java/v1/subproducts/",
          },
          {
            "variable_name": "url.ctas.status-endpoint",
            "url_text": "bcohmswrkctn01:8642/ctas-validacoes-java/v1/accounts/",
          },
          {
            "variable_name": "url.gagc.goods.endpoint",
            "url_text": "bcohmswrkctn01:8589/gagc-garantias-imoveis-java/v1/properties/warranties",
          },
          {
            "variable_name": "url.gagc.agreement.search",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements",
          },
          {
            "variable_name": "url.gagc.agreement.byid",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreement.status",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreementOperation",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreementsOperations/",
          },
          {
            "variable_name": "url.gagc.convenioguardachuva.inserirdadosconvenio.path",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.ged.pesquisar.obterdocumento",
            "url_text": "gedc-consultas-java.apps.ocp-h.original.com.br/v1/",
          },
          {
            "variable_name": "url.ged.inserir.documento",
            "url_text": "gedc-inclusao-manutencao-java.apps.ocp-h.original.com.br/v1/",
          },
          {
            "variable_name": "url.gagc.vincular.emprestimo.orq",
            "url_text": "bcohmswrkctn01:8706/gagc-orq-vinculacao-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.get.minutaria",
            "url_text": "bcohmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/",
          },
        ],
        "application-prd.properties": [
          {
            "variable_name": "url.cdps.customer.path",
            "url_text": "cdps-consultar-informacoes-cliente-java.original.com.br/v1",
          },
          {
            "variable_name": "url.gagc.product-endpoint",
            "url_text": "bcopmswrkctn01:8589/gagc-garantias-imoveis-java/v1/products",
          },
          {
            "variable_name": "url.gagc.subproduct-endpoint",
            "url_text": "bcopmswrkctn01:8589/gagc-garantias-imoveis-java/v1/subproducts/",
          },
          {
            "variable_name": "url.ctas.status-endpoint",
            "url_text": "bcopmswrkctn01:8642/ctas-validacoes-java/v1/accounts/",
          },
          {
            "variable_name": "url.gagc.goods.endpoint",
            "url_text": "bcopmswrkctn01:8589/gagc-garantias-imoveis-java/v1/properties/warranties",
          },
          {
            "variable_name": "url.gagc.agreement.search",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements",
          },
          {
            "variable_name": "url.gagc.agreement.byid",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreement.status",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreements/",
          },
          {
            "variable_name": "url.gagc.agreementOperation",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/agreementsOperations/",
          },
          {
            "variable_name": "url.gagc.convenioguardachuva.inserirdadosconvenio.path",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.ged.pesquisar.obterdocumento",
            "url_text": "gedc-consultas-java.original.com.br/v1/",
          },
          {
            "variable_name": "url.ged.inserir.documento",
            "url_text": "gedc-inclusao-manutencao-java.original.com.br/v1/",
          },
          {
            "variable_name": "url.gagc.vincular.emprestimo.orq",
            "url_text": "bcopmswrkctn01:8706/gagc-orq-vinculacao-convenio-guarda-chuva-java/v1",
          },
          {
            "variable_name": "url.get.minutaria",
            "url_text": "bcopmswrkctn01:8590/gagc-convenio-guarda-chuva-java/v1/",
          },
        ],
        "application.properties": [],
      },
    },
    "conv-conciliacao-detran-sp-batch-java": {
      "feign": [],
      "bootstrap": [],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "187.9.76.122:8901/Pagamento/ConsultarPagamento",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "187.9.76.122:8901/Pagamento/ConsultarPagamento",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "192.168.33.5:8090/Pagamento/ConsultarPagamento",
          }
        ],
        "application.properties": [],
      },
    },
    "conv-liquidacoes-detran-java": {
      "feign": [],
      "bootstrap": [
        {"integrations": "original-legacy; conv-corp; conv-integration"}
      ],
      "application": {
        "application-dev.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "187.9.76.122:8901",
          }
        ],
        "application-hml.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "187.9.76.122:8901",
          }
        ],
        "application-prd.properties": [
          {
            "variable_name": "daycoval.url.base",
            "url_text": "192.168.33.5:8090",
          }
        ],
        "application.properties": [],
      },
    },
    "ctad-ad-core-conv-convenios": {
      "feign": [],
      "bootstrap": [],
      "application": {},
    },
  }
}
