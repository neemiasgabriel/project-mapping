import re

text = """
package br.com.original.apio.services.feign;

import br.com.original.apio.config.FeignConfig;
import br.com.original.apio.model.ResponseData;
import br.com.original.apio.model.StandardRequest;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import static org.springframework.util.MimeTypeUtils.APPLICATION_JSON_VALUE;

@FeignClient(value = "registerPaymentDigitalWithdrawal", url = "${atmo.cmm.servcore.digital.with.drawal}", configuration = FeignConfig.class)
public interface DigitalWithDrawalServcore {

    @PostMapping(value = "/servcore/ms/registerPayment",
            consumes = APPLICATION_JSON_VALUE,
            produces = APPLICATION_JSON_VALUE)
    ResponseData confirmPayment(@RequestBody StandardRequest body);
}
"""

regex = r"url\s*=\s*(?P<url_text>.*?),"
match = re.search(regex , text)

if match:
  url_text = match.group("url_text")
  print("Extracted text:", url_text)