# Fabric Completely Overhauled: Archiving Repo
## Now Uses Go + Improved Install/Setup
### Review Updated Fabric Repo: Follow Instructions There. Enjoy! 

1. Clone Fabric https://github.com/danielmiessler/fabric to your local dev system and follow the installation directions.
    - You'll have to install pipx, if you only use pip3, as well as Python 3.10 at minimum.
    - Have your ChatGPT API key ready. 
    - The YouTube transcription features are amazing. I suggest generating a YouTube API key prior to setup.
    - I found the install to be a snap. 
    - The NetworkChuck video on the Fabric repo is definitely worth watching. 
2. Play around with just Fabric until you get a sense of how it works. 
    - On Ubuntu Linux I had to use `xclip` for clipboard functions, not `pbpaste`. This applies to Fabric only. 
    - The pdfprocess.py script uses the `pyperclip` module for copy/paste. You don't need `pyperclip` to use Fabric itself and are advised not to.
    - There's heavy activity on the Fabric repo currently, so at least weekly, you'll need to run `git pull` and `fabric --update` in the patterns directory.
    - They've been saying they plan to migrate to Go since May. You'll have the best experience using Linux.
3. Clone this repo into its own directory.
    - Ensure that the Python modules in requirements.txt are installed.
4. To run the pdfprocess.py script, both the script and the PDFs to process must be copied to the fabric/patterns directory.
    - Create a "sourcePDFs" directory inside fabric/patterns. 
    - Copy the PDFs you want to process into that directory. There's no limit on how many, other than how much you're willing to be billed for your ChatGPT API key usage. It's not expensive to run.
    - Copy the pdfprocess.py script from this locally-cloned repo to the root of the fabric/patterns directory.
    - Run the script inside fabric/patterns: `python3 pdfprocess.py`
    - This process could be optimized, but I only have so much time. I'm welcome to feedback on improvments. 
5. Please create an issue if you run into problems. 

# Sample Output - SUMMARIZE PATTERN

A successful output will name the 3 Fabric patterns prior to each pattern output, along with the Fabric repo URL. These and all 3 pattern outputs should be then be pre-pended to a new PDF, followed by a copy of the entire original PDF. The output file will have a "summarized_" prefix.

## Example

CHATGPT SUMMARY CREATED BY https://github.com/danielmiessler/fabric
----- USING **SUMMARIZE** FABRIC PATTERN

### ONE SENTENCE SUMMARY:
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

### MAIN POINTS:
1. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
2.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
3. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### TAKEAWAYS:
1. Un nulla posuere sollicitudin aliquam ultrices sagittis orci. Sit amet nisl suscipit adipiscing. 
2. Tincidunt dui ut ornare lectus sit amet est placerat in. 
3. Risus ultricies tristique nulla aliquet enim tortor at. 

# Sample Output - CREATE_REPORT_FINDING PATTERN

CHATGPT SUMMARY CREATED BY https://github.com/danielmiessler/fabric
----- USING **CREATE_REPORT_FINDING** FABRIC PATTERN

## Title: [Title]

### Description:
Orci dapibus ultrices in iaculis nunc sed augue. Dictum sit amet justo donec. Nisl pretium fusce id velit ut. Semper feugiat nibh sed pulvinar proin. Cursus sit amet dictum sit amet justo. Porta non pulvinar neque laoreet. Purus ut faucibus pulvinar elementum integer. Ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at. Sed enim ut sem viverra aliquet eget.

### Risk:
ed turpis tincidunt id aliquet risus feugiat in ante. Ornare lectus sit amet est placerat in egestas. Convallis aenean et tortor at risus viverra adipiscing at. Tortor posuere ac ut consequat semper viverra nam libero justo. Felis bibendum ut tristique et egestas quis ipsum. Turpis massa sed elementum tempus. Etiam tempor orci eu lobortis elementum nibh tellus.

### Recommendations:
- Pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl. 
- IArcu dictum varius duis at consectetur lorem donec. 
- Consectetur adipiscing elit duis tristique sollicitudin nibh sit amet. 

### References:
#### There may not be references to pull. If so, the output will inform you.
- "Understanding Building Water Leaks: Prevention and Remediation Strategies" by Building
Science Corporation
- "Water Intrusion in Buildings: Identifying, Preventing, and Remediating Issues" by ASTM
International
- "Guidelines for the Prevention of Water Intrusion in Buildings" by American Society of Civil
Engineers

### One-Sentence-Summary:
**NEW WINDOWS ARE NECESSARY.**

### Trends:
- Pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl. 
- IArcu dictum varius duis at consectetur lorem donec. 
- Consectetur adipiscing elit duis tristique sollicitudin nibh sit amet. 

### Quotes:
- "Major leak in base sill to units below; improper jamb weeps; air entry."
- "Water runs inside window system and to floors below."
- "Leak through anchors, probably at end dam."
- "Leaks at base and onto floor."
- "Bad water stains under window on floor."
- "Water from above and adjacent living room window seeps into closet and damaged cedar floor."
- "Water leak from water test in unit above."
- "Slider not closing properly."
- "Moisture in living room floor, leaking four feet out from kitchen wall."
- "Rain leak at patio doors damaging living room ceiling."
- "Leak by sliding door in living rooms upper left corner by ceiling."

# Sample Output - EXTRACT_REFERENCES PATTERN

CHATGPT SUMMARY CREATED BY https://github.com/danielmiessler/fabric
----- USING **EXTRACT_REFERENCES** FABRIC PATTERN

- [Understanding Building Envelope Failures](https://www.buildingenvelope.org)
- [Effective Waterproofing Techniques](https://www.waterproofingmagazine.com)
- [Maintenance Tips for Preventing Water Damage](https://www.propertymaintenance.com)
- [Guide to Window and Door Waterproofing](https://www.architecturaldigest.com)

