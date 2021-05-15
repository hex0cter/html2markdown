from mercy_reader import reader

def handler(event, context):
    print(f"event: {event}")
    print(f"context: {context}")

    obj = reader.main(
        event,
        80,
    )
    return reader.Format.formatter['md'](obj)


    # rc = event["requestContext"]
    # servicePath = rc["path"][:-len(rc["resourcePath"])] # path minus the resource path '/greet'

    # GET from the /time endpoint
    # connection = http.client.HTTPSConnection(event["headers"]["Host"])
    # connection.request("GET", "{0}/time".format(servicePath))
    # timestamp = connection.getresponse().read().decode()
    # time_str = datetime.fromtimestamp(int(timestamp)).strftime("%B %d, %Y")

    # return {
    #     "statusCode": 200,
    #     "body": "I am the second lambda"
    #     # "body": "<html><body><p>Hello! It is now {0}.</p></body></html>".format("time_str"),
    #     # "headers": {
    #     #     "Content-Type": "text/html"
    #     # }
    # }
