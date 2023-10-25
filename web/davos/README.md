# Davos
## Concept
WebDAV-enabled application with public and private (password-protected) endpoint.

## Solution
- Upload reverse shell into public endpoint of the WebDAV
- Use RCE to leak source code of health-check.php, inside there is a credentials to access the private WebDAV
- Get flag from the private WebDAV