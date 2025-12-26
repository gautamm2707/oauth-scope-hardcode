# OCI API Gateway + Authorizer Function for OIC Token Generation Without OAuth Scopes

This project demonstrates how to use OCI API Gateway and an OCI Function to generate OCI IAM (IDCS) tokens for OIC integrations without requiring OAuth scopes from the client.

This solves a real-world industry problem where external partners and legacy systems cannot append OAuth scopes, even though IDCS requires them for Client Credentials flow.

The Authorizer Function injects the correct OIC scope internally, acting as a token broker.
