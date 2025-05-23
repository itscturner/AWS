Image Pipeline
---
<h3>Step 1: Specifiy Pipeline Details</h3>

**Pipeline Name:** RPMISO<br>
**Description:** "Download RPM Updates."<br>

**Build Schedule:** Manual<br>
<br>

---

<h3>Step 2: Choose Recipe</h3>

**Use Existing Recipe:** RPMISO<br>
<br>

---

<h3>Step 3: Define Image Creation Process</h3>

**Default Workflows** <br>
<br>

---

<h3>Step 4: Define Infrastructure Configuration</h3>

**Create A New Infrastructure Configuration**: <br>
**Name:** RPMISO<br>
**IAM Role:** EC2InstanceProfileForImageBuilder<br>
**Instance Type:** t3.medium<br>
<br>

---

<h3>Step 5: Define Distribution Settings</h3>

**Create New Distribution Settings:** <br>
**Name:** RPMISO <br>
**Region:** us-west-1 <br>
