fernanda_project_acronym = ['acad', 'apio', 'cdps', 'ctas', 'fepw', 'parc', 'rtto', 'tbgr', 'trfo', 'atmo', 'gcen',
                            'mcsv', 'ctasm']
other_projects_acronym = ['cbic', 'conv', 'depb', 'pgto', 'port', 'trnf', 'alcd', 'antv', 'atad', 'atcl', 'atco',
                          'atfd', 'atkn', 'clbk', 'herm', 'retr', 'bpmo', 'gedc', 'pvfr', 'pvld', 'aant', 'bimo',
                          'cess', 'crgr', 'crmd', 'epat', 'fdos', 'gagc', 'glcr', 'glpf', 'glpj', 'intr', 'inve',
                          'invo', 'mbio', 'prev', 'tsbo']
relevant_files = ['application.properties', 'application-hml.properties', 'application-dev.properties',
                  'application-prd.properties', 'bootstrap.yml']

fernanda_projects_dictionary = {
  "acad": {
    "acad-consultas-dominios-java": [
      {
        "file": "DominioClient.java",
        "path": "src/main/java/br/com/original/acad/feign/DominioClient.java",
        "url": 'original.url.rest.consultation.dominios',
      }
    ]
  },
  "apio": {
    "apio-canal-saque-digital-java": [
      {
        "file": "DigitalWithDrawalServcore.java",
        "path": "src/main/java/br/com/original/apio/services/feign/DigitalWithDrawalServcore.java",
        "url": 'atmo.cmm.servcore.digital.with.drawal',
      }
    ],
    "apio-canal-extratos-parceiro-java": [],
    "apio-consultas-debito-automatico-java": [
      {
        "file": "ConsultationAutomaticDebitClient.java",
        "path": "src/main/java/br/com/original/apio/feign/conv/ConsultationAutomaticDebitClient.java",
        "url": 'conv.consultas.debito.automatico.java.url',
      }
    ],
    "apio-solicitacao-cartao-java": [],
    "apio-boletos-parceiro-java": [
      {
        "file": "SlipFeign.java",
        "path": "src/main/java/br/com/original/apio/feign/SlipFeign.java",
        "url": 'cbic.slip.url',
      }
    ],
    "apio-canal-cartao-pre-pago-virtual-java": [
      {
        "file": "CardFeignClient.java",
        "path": "src/main/java/br/com/original/apio/feign/CardFeignClient.java",
        "url": 'url.virtual.card',
      }
    ],
    "apio-canal-abertura-cadastro-java": [
      {
        "file": "RegistersFeign.java",
        "path": "src/main/java/br/com/original/apio/cdps/orq/abertura/cadastro/feign/RegistersFeign.java",
        "url": 'registers.request.url',
      }
    ],
  },
  "cdps": {
    "cdps-tratamento-cep-java": [
      {
        "file": "FindCep.java",
        "path": "src/main/java/br/com/original/cdps/feign/FindCep.java",
        "url": 'cep.request.url',
      }
    ],
    "cdps-manutencao-prospect-java": [],
    "cdps-documentos-nao-correntista-java": [],
    "cdps-orq-dados-cadastrais-java": [],
    "cdps-officer-java": [
      {
        "file": "CustomerAcadFeignService.java",
        "path": "src/main/java/br/com/original/cdps/services/feign/CustomerAcadFeignService.java",
        "url": 'acad.apoio.cadastro.url',
      }
    ],
    "cdps-empresas-java": [
      {
        "file": "CdpsSearchClientInfos.java",
        "path": "src/main/java/br/com/original/cdps/services/feign/CdpsSearchClientInfos.java",
        "url": 'cdps.consultar.informacoes.cliente.java.url',
      }
    ],
    "cdps-cmm-rest-java": [
      {
        "file": "ProspectAcadServiceFeign.java",
        "path": "src/main/java/br/com/original/cdps/services/feign/ProspectAcadServiceFeign.java",
        "url": 'original.acad.consulta.url',
      }
    ],
    "cdps-atualizar-cadastro-java": [
      {
        "file": "FindSolicitarCartaoClient.java",
        "path": "src/main/java/br/com/original/atualizar/cadastro/feign/FindSolicitarCartaoClient.java",
        "url": 'url.servico.solicitarCartao',
      }
    ],
  },
  "ctas": {
    "ctas-abertura-conta-vinculada-cmm-java": [],
    "ctas-credito-imediato-java": [],
    "ctas-cmm-rest-java": [],
    "ctas-solicita-encerramento-java": [
      {
        "file": "RttoEncerraChequeEspecialFeignService.java",
        "path": "src/main/java/br/com/original/ctas/feign/RttoEncerraChequeEspecialFeignService.java",
        "url": 'original.url.rest.cheque-especial-java-url',
      }
    ],
  },
  "fepw": {"fepw-cmm-rest-java": []},
  "parc": {
    "apio-canal-extratos-parceiro-java": [],
    "mcsv-interno-consulta-parcelados-java": [],
    "apio-boletos-parceiro-java": [
      {
        "file": "SlipFeign.java",
        "path": "src/main/java/br/com/original/apio/feign/SlipFeign.java",
        "url": 'cbic.slip.url',
      }
    ],
  },
  "rtto": {
    "rtto-consultar-contrato-cheque-especial-java": [
      {
        "file": "CtasSaldoFeign.java",
        "path": "src/main/java/br/com/original/rtto/service/feign/CtasSaldoFeign.java",
        "url": 'original.url.ctas.saldo.java',
      }
    ],
    "rtto-repactuacao-taxas-batch-java": [
      {
        "file": "SincronizationTableClientInterface.java",
        "path": "src/main/java/br/com/original/rtto/feign/interfaces/SincronizationTableClientInterface.java",
        "url": 'tbgr.sincronizacao.tabelas.java.url',
      }
    ],
    "rtto-consumer-manutencao-limites-java": [],
    "rtto-consultar-cheque-especial-java": [
      {
        "file": "CrplDominiosFeign.java",
        "path": "src/main/java/br/com/original/rtto/service/feign/CrplDominiosFeign.java",
        "url": 'original.url.crpl.dominios.java',
      }
    ],
    "mcsv-rtto-cheque-empresarial-java": [
      {
        "file": "RetentionFeignClientService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/RetentionFeignClientService.java",
        "url": 'url.api.retention',
      }
    ],
  },
  "tbgr": {
    "tbgr-canal-cartorios-java": [
      {
        "file": "NotaryOfficesServiceFeign.java",
        "path": "src/main/java/br/com/original/services/feign/NotaryOfficesServiceFeign.java",
        "url": 'url.rest.cartorio}/v1/notary-offices"',
      }
    ]
  },
  "trfo": {"trfo-cmm-rest-java": []},
  "atmo": {
    "atmo-hub-digital-java": [
      {
        "file": "ServcoreClient.java",
        "path": "src/main/java/br/com/original/atmo/feign/ServcoreClient.java",
        "url": 'url.servcore',
      }
    ]
  },
  "gcen": {},
  "mcsv": {
    "mcsv-cobranca-tarifas-java": [
      {
        "file": "GetValueRateFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/GetValueRateFeignService.java",
        "url": 'cbic.tarifas.java.url',
      }
    ],
    "mcsv-open-banking-handoff-java": [
      {
        "file": "OpbkConsentClient.java",
        "path": "src/main/java/br/com/original/mcsv/feign/OpbkConsentClient.java",
        "url": 'opbk.consentimentos.java.url',
      }
    ],
    "mcsv-interno-renegociacao-posvenda-java": [
      {
        "file": "PaymentsClient.java",
        "path": "src/main/java/br/com/original/mcsv/feign/PaymentsClient.java",
        "url": 'empc.orq.pagamento.parcelado.java.url',
      }
    ],
    "mcsv-interno-consulta-saldo-java": [
      {
        "file": "SaldoFeingService.java",
        "path": "src/main/java/br/com/original/mcsv/controller/request/feign/SaldoFeingService.java",
        "url": 'ctas.saldo.java.url',
      }
    ],
    "mcsv-interno-dominios-java": [
      {
        "file": "DomainsFeign.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/DomainsFeign.java",
        "url": 'tbgr.dominios.java.url',
      }
    ],
    "mcsv-consulta-dossie-java": [
      {
        "file": "ConsultaDossieFeign.java",
        "path": "src/main/java/br/com/original/mcsv/feign/ConsultaDossieFeign.java",
        "url": 'original.url.consulta.dossie',
      }
    ],
    "mcsv-interno-bens-cadastrados-java": [],
    "mcsv-interno-consulta-cessao-credito-java": [
      {
        "file": "CreditInstalmentFeign.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/CreditInstalmentFeign.java",
        "url": 'cess.consulta.transacoes.java.url',
      }
    ],
    "mcsv-interno-consulta-parcelados-java": [],
    "mcsv-converter-informacoes-cliente-java": [
      {
        "file": "SublimitsCustomerConsumerFeign.java",
        "path": "src/main/java/br/com/original/mcsv/consumer/feign/SublimitsCustomerConsumerFeign.java",
        "url": 'glpf.consulta.limites.java.url',
      }
    ],
    "mcsv-informacoes-atendimento-java": [
      {
        "file": "CtrcFeingClient.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/CtrcFeingClient.java",
        "url": 'ctcr.consultas.conta.cartao.java.url',
      }
    ],
    "mcsv-interno-consulta-credito-rotativos-java": [
      {
        "file": "RttoOperacoesFeign.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/RttoOperacoesFeign.java",
        "url": 'rtto.operacoes.java.url',
      }
    ],
    "mcsv-consulta-contrato-renegociado-java": [],
    "mcsv-interno-consultas-bpmo-java": [
      {
        "file": "CoholdersProspectionAttemptsFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/domain/coholder_attempts/service/feign/CoholdersProspectionAttemptsFeignService.java",
        "url": 'bpmo.incluir.cotitular.java.url',
      }
    ],
    "mcsv-aprovacao-proposta-java": [
      {
        "file": "RenegotiationProposalFeign.java",
        "path": "src/main/java/br/com/original/feign/RenegotiationProposalFeign.java",
        "url": 'rnco.aprovacao.proposta.java.url',
      }
    ],
    "mcsv-consulta-contas-rewards-java": [
      {
        "file": "RewardsCustomersService.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/RewardsCustomersService.java",
        "url": 'feign.orchestration.rewards.balance.client',
      }
    ],
    "mcsv-cheque-especial-java": [
      {
        "file": "RttoConsultaChequeEspecialFeign.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/RttoConsultaChequeEspecialFeign.java",
        "url": 'original.url.rtto.consultar.cheque.especial.java',
      }
    ],
    "mcsv-interno-parametrizacao-perfis-java": [],
    "mcsv-carteira-cobranca-digital-java": [
      {
        "file": "GetDigitalWalletFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/GetDigitalWalletFeignService.java",
        "url": 'cbic.carteira.cobranca.digital.java.url',
      }
    ],
    "mcsv-topaz-java": [
      {
        "file": "ScoreFeign.java",
        "path": "src/main/java/br/com/original/mcsv/feign/ScoreFeign.java",
        "url": 'pvfr.topaz.java.url',
      }
    ],
    "mcsv-cobranca-lote-java": [
      {
        "file": "UploadDocumentAntvFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/UploadDocumentAntvFeignService.java",
        "url": 'cbic.cobranca.lote.java.url',
      }
    ],
    "mcsv-interno-consulta-grupos-relacionamento-java": [
      {
        "file": "GroupFeign.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/GroupFeign.java",
        "url": 'cdps.consulta.grupos.relacionamento.java.url',
      }
    ],
    "mcsv-consultas-cartoes-java": [],
    "mcsv-consulta-credito-pessoal-java": [
      {
        "file": "LoanLimitFeign.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/LoanLimitFeign.java",
        "url": 'original.url.crpl.consulta-limites-java',
      }
    ],
    "mcsv-interno-renegociacao-dividas-correntista-java": [],
    "mcsv-relatorio-visitas-pvld-java": [
      {
        "file": "RelatorioVisitaFeign.java",
        "path": "src/main/java/br/com/original/mcsv/feign/RelatorioVisitaFeign.java",
        "url": 'original.url.relatorio.visitas',
      }
    ],
    "mcsv-interno-atendimento-java": [],
    "mcsv-pag-original-java": [
      {
        "file": "PagForFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/PagForFeignService.java",
        "url": 'original.url.rest.pgto-pag-original',
      }
    ],
    "mcsv-autenticacao-pj-java": [],
    "mcsv-credito-limites-java": [
      {
        "file": "CreditLimitFeign.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/CreditLimitFeign.java",
        "url": 'original.url.glpf.limites.credito.java',
      }
    ],
    "mcsv-renegociacao-dividas-java": [],
    "mcsv-proposta-java": [],
    "mcsv-dados-cadastrais-pu-java": [],
    "mcsv-documentos-java": [
      {
        "file": "GedcInclusaoServiceFeign.java",
        "path": "src/main/java/br/com/original/mcsv/documentos/services/feign/GedcInclusaoServiceFeign.java",
        "url": 'original.url.rest.gedc-inclusao',
      }
    ],
    "mcsv-pagamento-faturas-java": [
      {
        "file": "InvoicePaymentFeignClient.java",
        "path": "src/main/java/br/com/original/ctcr/feign/InvoicePaymentFeignClient.java",
        "url": 'rest.api.invoicepayments',
      }
    ],
    "mcsv-interno-atualizacao-cadastral-java": [
      {
        "file": "PhoneConsumerFeign.java",
        "path": "src/main/java/br/com/original/mcsv/webclient/cdps/consumer/feign/PhoneConsumerFeign.java",
        "url": 'cdps-atualizacao-dados-cadastrais-java.url',
      }
    ],
    "mcsv-permissao-optin-java": [
      {
        "file": "PermissionFeignService.java",
        "path": "src/main/java/br/com/original/intr/mcsv/service/feign/PermissionFeignService.java",
        "url": 'intr.permissao.optin.java.url',
      }
    ],
    "mcsv-interno-contato-cadastro-java": [],
    "mcsv-notificacoes-inbox-java": [
      {
        "file": "CenoNotificacoesInboxFeign.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/CenoNotificacoesInboxFeign.java",
        "url": 'original.url.ceno.notificacoes.inbox.java',
      }
    ],
    "mcsv-interno-manifestacao-java": [
      {
        "file": "ManifestationFeignService.java",
        "path": "src/main/java/br/com/original/services/feign/ManifestationFeignService.java",
        "url": 'original.gmnf.manifestacao.url',
      }
    ],
    "mcsv-liveness-appkey-java": [
      {
        "file": "LivenessChallengeApiService.java",
        "path": "src/main/java/br/com/original/mcsv/esqueciminhasenha/service/feign/LivenessChallengeApiService.java",
        "url": 'retr.desafios.liveness.java.url',
      }
    ],
    "mcsv-interno-informe-rendimentos-java": [],
    "mcsv-autenticacao-area-nao-logada-java": [
      {
        "file": "CustomerInfoApiService.java",
        "path": "src/main/java/br/com/original/mcsv/autenticacao/services/feign/CustomerInfoApiService.java",
        "url": 'cdps.consultar.informacoes.endpoint',
      }
    ],
    "mcsv-interno-consultas-callback-java": [],
    "mcsv-interno-analise-callback-java": [],
    "mcsv-interno-consultas-pix-java": [],
    "mcsv-interno-capital-giro-java": [],
    "mcsv-interno-cobranca-digital-java": [
      {
        "file": "StandardAccountsRestFeingService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/StandardAccountsRestFeingService.java",
        "url": 'cbic.cobranca.expressa.java.url',
      }
    ],
    "mcsv-interno-positivacao-cliente-java": [
      {
        "file": "AuthFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/positivacao/cliente/service/feign/AuthFeignService.java",
        "url": 'atcl.auth.corporate.java.url"',
      }
    ],
    "mcsv-interno-investimentos-java": [],
    "mcsv-interno-seguros-java": [
      {
        "file": "InsuranceFeignService.java",
        "path": "src/main/java/br/com/original/insurance/services/feign/InsuranceFeignService.java",
        "url": 'cosg.cmm.rest.java.url',
      }
    ],
    "mcsv-parametrizacao-rewards-java": [
      {
        "file": "ScoreRangeParametersFeignClient.java",
        "path": "src/main/java/br/com/original/mcsv/feign/ScoreRangeParametersFeignClient.java",
        "url": 'url.score.range.parameters',
      }
    ],
    "mcsv-interno-prospects-java": [],
    "mcsv-interno-contatos-java": [],
    "mcsv-interno-pagamentos-java": [],
    "mcsv-interno-gestao-limite-credito-java": [],
    "mcsv-cadastro-pep-fatca-java": [
      {
        "file": "CdpsCadastroPepFatcaRestService.java",
        "path": "src/main/java/br/com/original/feign/CdpsCadastroPepFatcaRestService.java",
        "url": 'original.url.rest.cdps-cadastro-pep-fatca',
      }
    ],
    "mcsv-interno-contas-java": [
      {
        "file": "DepositCMMFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/DepositCMMFeignService.java",
        "url": 'ctas.cmm.rest.java.url',
      }
    ],
    "mcsv-abertura-conta-java": [
      {
        "file": "ProviderFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/domain/provider/feign/ProviderFeignService.java",
        "url": 'reip.cadastro.pf.java.url',
      }
    ],
    "mcsv-token-atendimento-java": [],
    "mcsv-interno-tarefas-ofertas-java": [],
    "mcsv-interno-agenda-comercial-java": [],
    "mcsv-clientes-java": [],
    "mcsv-interno-retencao-callback-java": [],
    "mcsv-rtto-cheque-empresarial-java": [
      {
        "file": "RetentionFeignClientService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/RetentionFeignClientService.java",
        "url": 'url.api.retention',
      }
    ],
    "mcsv-plat-cheque-empresarial-java": [
      {
        "file": "ContractingOperationsFeignClientService.java",
        "path": "src/main/java/br/com/original/mcsv/services/feign/ContractingOperationsFeignClientService.java",
        "url": 'url.api.rtto',
      }
    ],
    "mcsv-interno-atividades-bpmo-java": [],
    "mcsv-capital-giro-java": [
      {
        "file": "SlipSearchesFeign.java",
        "path": "src/main/java/br/com/original/feign/SlipSearchesFeign.java",
        "url": 'cbic.boletos.java.url',
      }
    ],
    "mcsv-pagamentos-java": [
      {
        "file": "ScheduledFeingService.java",
        "path": "src/main/java/br/com/original/pagamentos/services/feign/ScheduledFeingService.java",
        "url": 'original.url.payments.url.base',
      }
    ],
    "mcsv-interno-credito-java": [],
    "mcsv-interno-documentos-java": [
      {
        "file": "IncludeDocumentFeign.java",
        "path": "src/main/java/br/com/original/mcsv/documentos/services/feign/IncludeDocumentFeign.java",
        "url": 'gedc.inclusao.manutencao.java.url',
      }
    ],
    "mcsv-interno-gerentes-java": [],
    "mcsv-interno-cadastro-java": [],
    "mcsv-cobranca-expressa-java": [
      {
        "file": "SlipModelClient.java",
        "path": "src/main/java/br/com/original/mcsv/feign/SlipModelClient.java",
        "url": 'cbic.modelos.boleto.java.url',
      }
    ],
    "mcsv-token": [
      {
        "file": "HermClient.java",
        "path": "src/main/java/br/com/original/mcsv/feign/HermClient.java",
        "url": 'herm.url',
      }
    ],
    "mcsv-bootstrap-java": [],
  },
  "ctasm": {},
}

other_projects_dictionary = {
  "cbic": {},
  "conv": {
    "mcsv-converter-informacoes-cliente-java": [
      {
        "file": "SublimitsCustomerConsumerFeign.java",
        "path": "src/main/java/br/com/original/mcsv/consumer/feign/SublimitsCustomerConsumerFeign.java",
        "url": "glpf.consulta.limites.java.url",
      }
    ]
  },
  "depb": {},
  "pgto": {
    "pgto-ordem-pagamento-pix-java": [],
    "pgto-cancela-baixa-titulos-pagfor-java": [],
    "pgto-cmm-rest-java": [],
  },
  "port": {},
  "trnf": {},
  "alcd": {},
  "antv": {},
  "atad": {},
  "atcl": {},
  "atco": {},
  "atfd": {},
  "atkn": {},
  "clbk": {},
  "herm": {},
  "retr": {},
  "bpmo": {
    "mcsv-interno-consultas-bpmo-java": [
      {
        "file": "CoholdersProspectionAttemptsFeignService.java",
        "path": "src/main/java/br/com/original/mcsv/domain/coholder_attempts/service/feign/CoholdersProspectionAttemptsFeignService.java",
        "url": "bpmo.incluir.cotitular.java.url",
      }
    ],
    "mcsv-interno-atividades-bpmo-java": [],
  },
  "gedc": {},
  "pvfr": {},
  "pvld": {
    "mcsv-relatorio-visitas-pvld-java": [
      {
        "file": "RelatorioVisitaFeign.java",
        "path": "src/main/java/br/com/original/mcsv/feign/RelatorioVisitaFeign.java",
        "url": "original.url.relatorio.visitas",
      }
    ]
  },
  "aant": {},
  "bimo": {},
  "cess": {
    "mcsv-interno-consulta-cessao-credito-java": [
      {
        "file": "CreditInstalmentFeign.java",
        "path": "src/main/java/br/com/original/mcsv/service/feign/CreditInstalmentFeign.java",
        "url": "cess.consulta.transacoes.java.url",
      }
    ]
  },
  "crgr": {},
  "crmd": {},
  "epat": {},
  "fdos": {},
  "gagc": {},
  "glcr": {},
  "glpf": {},
  "glpj": {},
  "intr": {},
  "inve": {"mcsv-interno-investimentos-java": []},
  "invo": {},
  "mbio": {},
  "prev": {},
  "tsbo": {},
}
