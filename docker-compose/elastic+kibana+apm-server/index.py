import elasticapm
client = elasticapm.Client(service_name = 'APM_SERVER_DEMO' ,server_url ='http://localhost:8200', elastic_apm_active = "true" ) 

def main():
    print("Hi")
    client.capture_message( "hello world! I'm a demo" )

def apmCaptureMessage(message):
    client.capture_message(message)

def apmInstrument():
    elasticapm.instrument()

def apmBeginTransaction(transName):
    client.begin_transaction(transName)

def apmEndTransaction(transName):
    client.end_transaction(transName)

if __name__ == "__main__": 
    apmInstrument()
    apmBeginTransaction("pickslip_th")
    main()
    apmEndTransaction("pickslip_th")