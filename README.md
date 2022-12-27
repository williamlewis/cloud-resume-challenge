# cloud-resume-challenge
Repo to track progress and document the outcome of my Cloud Resume Challenge project


## Challenge Steps & Progress:

- [x]  1. Earn an **AWS Certification**
    - passed CCP in September, the CSA Associate in October

- [x]  2. Write Resume in **HTML**
    - utilized Bootstrap framework for general organization & positioning
    - recreated a sample from scratch (instead of a downloaded template)

- [x]  3. Style Resume in **CSS**
    - used selective overrides on top of Bootstrap framework

- [x]  4. Deploy Resume to Static Website with **AWS S3**
    - utilized OAC origin access control to improve security by restricting access to CloudFront distribution
    - left public access blocked & static website feature disabled for compatibility with OAC

- [x]  5. Use HTTPS Protocol with **AWS CloudFront**
    - redirects any HTTP requests to HTTPS
    - IPv6 enabled in addition to IPv4
    - SSL certificate validated for root domain and `*.` subdomains

- [x]  6. Point Custom DNS Domain Name with **AWS Route 53**
    - custom domain purchased through **Cloudflare** (not Route 53)
    - validation CNAME records needed in Cloudflare DNS settings
    - CNAME / A / AAAA alias records not needed in Route 53 for successful DNS resolution
    - website successfully loads from multiple browsers, with & without `www.` subdomain

- [ ]  7. Create a Webpage Visitor Counter with **Javascript**

- [ ]  8. Create a Visitor Counter Database with **AWS DynamoDB**

- [ ]  9. Connect Webpage to Database with **AWS API Gateway + Lambda**

- [ ] 10. Write a Lambda Function with **Python + AWS Boto3 SDK**

- [ ] 11. Perform **Tests** on Python Code

- [ ] 12. Configure Resources with **IaC Using an AWS SAM Template**

- [ ] 13. Utilize **Source Control** with GitHub

- [ ] 14. Implement **Backend CI/CD** for SAM Template with GitHub Actions

- [ ] 15. Implement **Frontend CI/CD** for Webpage Content with GitHub Actions

- [ ] 16. Share Your Challenges and Learnings with a **Dev.to Blog Post**

