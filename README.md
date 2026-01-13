# OCI API Gateway + Authorizer Function for OIC Token Generation Without OAuth Scopes

OCI Function to hardcode SCOPE before invoking OCI IAM token endpoints in order to access OIC REST Endpoints via API Gateway. This repo is the code for my blog post https://www.ateam-oracle.com/securing-oic-apis-for-legacy-clients-using-oauth-without-scopes

This project demonstrates how to use OCI API Gateway and an OCI Function to generate OCI IAM (IDCS) tokens for OIC integrations without requiring OAuth scopes from the client.

This solves a real-world industry problem where external partners and legacy systems cannot append OAuth scopes, even though OCI IA< requires them for Client Credentials flow.

The Authorizer Function injects the correct OIC scope internally, acting as a token broker.

# Running the script
how to run in OCI:

Login to OCI Tenancy
Create an OCI Function. https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm
fn init --runtime python CacheToken, then press Enter.
Navigate to the function directory, open the func.py file, and seamlessly replace the existing code snippet with the func.py.
Include the requirements from the requirements.txt file
Navigate to the function folder and run the following command fn -v deploy --app to deploy it.
