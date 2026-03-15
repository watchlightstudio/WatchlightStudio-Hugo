---
linkTitle: "Notion setup"
type: docs
weight: 6
url: "/nucleate/setup-and-compatibility/notion"
---
## Notion setup

Nucleate integrates with Notion using an API and requires some pre-setup before it will push files to the cloud. Follow the below instructions and screenshots to get connected.

### 1. Initialize a new database
Create a new private page.
<img src="/notion/01_new_database.png">
Make a new "Database" to push your Nucleate summaries.
<img src="/notion/02_new_database.png">

### 2. Setup the database columns
{{< callout type="info" >}}  
You can name the database anything, but the database columns must match the labels and column types exactly as shown below.
{{< /callout >}}
Name your new database anything you want.
<img src="/notion/03_setup_database.png">
Set the first column to be "Name". It is likely set to this already by default.
<img src="/notion/04_setup_database.png">
Set the second column to be "Tags". It must be type "Multi-Select".
<img src="/notion/05_setup_database.png">
Set the third column to be "Date". It must be type "Date".
<img src="/notion/06_setup_database.png">
Set the fourth column to be "Type". It must be type "Select".
<img src="/notion/07_setup_database.png">
Set the final column to be "Last uploaded". It must be type "Date".
<img src="/notion/08_setup_database.png">

### 3. Setup Notion Integrations
Create a new integration.
<img src="/notion/09_integrations.png">
Provide an integration name and select the target workspace with the new database.
<img src="/notion/10_integrations.png">
The integration secret is needed to connect Nucleate and Notion. The secret is saved in plain text on your machine when connected to Nucleate.
<img src="/notion/11_integrations.png">
Edit access and select the appropriate database to which you push Nucleate summaries.
<img src="/notion/12_integrations.png">
<img src="/notion/13_integrations.png">

### 4. Connect to Nucleate
In the Nucleate "Integrations/Notion" panel, enable Notion Integration and paste your API secret. Paste the URL to your new Notion database into the "Analyze URL" analyzer.
<img src="/notion/14_nucleate.png">
If connected successfully. both API Status and Database Status will be green. If either is yellow or red, review the respective steps from above.
<img src="/notion/15_nucleate.png">
