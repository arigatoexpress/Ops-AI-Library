# FAQ

## For Operations Managers

### Do I need to be technical?
No. If you can copy, paste, and edit a draft email, you can use this library.

### Which tool should I use?
**Gemini Enterprise** if that is what your site has approved.  
If leadership designates another approved tool, the same prompts still work.

### Can I paste real tracking numbers or customer names?
**No** — not into unapproved or public tools.  
Use placeholders like `[Customer group]` and `[Issue category]`.  
Only use real data when the tool **and** workflow are approved for that classification.

### Will AI make my shift decisions?
No. **AI drafts. You decide.**  
You still own staffing, safety, customer, and network calls.

### What if the answer invents something?
Delete it. Put the item under **Needs verification**.  
Tell us via the feedback form/issue so we can harden the prompt or soul.

### Where do I start on day one?
1. [Manager wallet card](manager-wallet-card.md)  
2. [Prompt Explorer](../prompts/explorer.html) (open in a browser)  
3. First-week set: P01 · P02 · P08 · P15 · P20 · P44  

### Do I need GitHub?
No. Prefer the **Prompt Explorer** file or the future **SharePoint** site.  
GitHub is where the team maintains the source.

### Can I use this on my phone?
Yes for reading prompts and copying text, if policy allows the AI tool on mobile.  
Still scrub sensitive data.

---

## For Leadership / Program Owners

### Is this official FedEx policy?
No. It is an operations-led library that must stay aligned with company policy.

### Why not build another dashboard?
Managers adopt **prompts and agents** faster than multi-app monorepos.  
Dashboards/CLIs stay optional in the [appendix](../appendix/prior-example-projects.md).

### Are Power Automate agentic workflows live?
Not yet. Specs and playbooks are ready for when access and approval land.  
See [flow specs](../playbooks/power-automate-flow-specs.md).

### How do we measure success?
[Pilot scorecard](pilot-scorecard.md): weekly users, minutes saved, invented-fact reports, near misses.

### What is the 90-day plan?
[playbooks/90-day-roadmap.md](../playbooks/90-day-roadmap.md)

### Who owns content?
Name a content owner (prompts/souls), a site owner (SharePoint), and a tech owner (flows/GCP).  
See SharePoint playbook Phase 0 checklist.

---

## For Builders (Gemini / data)

### How do I create an agent?
[playbooks/gemini-enterprise-day-one.md](../playbooks/gemini-enterprise-day-one.md) + paste a [soul](../souls/README.md).

### Can the agent send email?
Not in v1. Draft only. Actions require approved workflow + human gate.

### What goes in the GCP sandbox first?
Synthetic metrics generator → eval harness → narrative helper.  
[playbooks/gcp-sandbox.md](../playbooks/gcp-sandbox.md)

### How do I update the Prompt Explorer after editing prompts?
```bash
node scripts/build-prompt-index.mjs
```
