import io
import json
import logging
from fdk import response
import requests

# Constants - replace with your actual values or read from ctx.Config()
TOKEN_URL = "https://idcs-ff3532e3a9ba4###########.identity.oraclecloud.com/oauth2/v1/token"
SCOPE = "https://01DB8CF84FDB4C##############.integration.us-ashburn-1.ocp.oraclecloud.com:443urn:opc:resource:consumer::all"

def handler(ctx, data: io.BytesIO = None):
    #initContext(dict(ctx.Config()))
    try:
        logging.getLogger().info("handler: Started Function Execution") 
        #gateway_auth = json.loads(data.getvalue())
        headers = ctx.Headers()
        auth_header = headers.get("authorization")
        
        # Authorization header must be provided in payload as "Authorization" field
        #auth_header = gateway_auth.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return response.Response(
                ctx,
                response_data=json.dumps({"error": "Missing or invalid Authorization header"}),
                status_code=400,
                headers={"Content-Type": "application/json"}
            )

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": auth_header
        }
        payload = {
            "grant_type": "client_credentials",
            "scope": SCOPE
        }
        # Call the OCI IAM/IDCS token endpoint
        token_response = requests.post(
            TOKEN_URL,
            headers=headers,
            data=payload,
            timeout=10  # avoid hanging
        )

        if token_response.status_code != 200:
            return response.Response(
                ctx,
                response_data=json.dumps({"error": "Token endpoint error", "details": token_response.text}),
                status_code=token_response.status_code,
                headers={"Content-Type": "application/json"}
            )

        return response.Response(
            ctx,
            response_data=token_response.text,
            status_code=200,
            headers={"Content-Type": "application/json"}
        )

    except Exception as ex:
        logging.getLogger().error("Exception occurred: " + str(ex))
        return response.Response(
            ctx,
            response_data=json.dumps({"error": str(ex)}),
            status_code=500,
            headers={"Content-Type": "application/json"}
        )
