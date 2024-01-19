## [Gpt Research](https://github.com/assafelovic/gpt-researcher?tab=readme-ov-file)
## Moteur de recherche [Tavily](https://docs.tavily.com/docs/examples/examples)

- Environnement conda gptresearch
- API key openAI et Tavily dans .env
- Accès avec:
```
from dotenv import load_dotenv
load_dotenv()
```
### Exemple 
- Avec le code:
```Python
import os
from dotenv import load_dotenv
load_dotenv()
from tavily import TavilyClient
# libraries
from langchain.adapters.openai import convert_openai_messages
from langchain.chat_models import ChatOpenAI
#os.environ
client = TavilyClient(os.environ["TAVILY_API_KEY"])
# simple query using tavily's advanced search
query="What happened in the latest burning man floods?"
content=client.search(query, search_depth="advanced")
#print(content)
# setup prompt
prompt = [{
    "role": "system",
    "content":  f'You are an AI critical thinker research assistant. '\
                f'Your sole purpose is to write well written, critically acclaimed,'\
                f'objective and structured reports on given text.'
}, {
    "role": "user",
    "content": f'Information: """{content}"""\n\n' \
               f'Using the above information, answer the following'\
               f'query: "{query}" in a detailed report --'\
               f'Please use MLA format and markdown syntax.'
}]

# run gpt-4
lc_messages = convert_openai_messages(prompt)
report = ChatOpenAI(model='gpt-4',openai_api_key=os.environ["OPENAI_API_KEY"]).invoke(lc_messages).content

# print report
print(report)
```
- Résultat:
# The Latest Burning Man Floods: A Detailed Report

The Burning Man festival, an annual event held in the Black Rock Desert of Nevada, experienced unprecedented flooding in its latest edition in September 2023. The flooding left thousands of attendees stranded, led to the investigation of a death at the site, and caused significant disruptions in the festival's concluding events.

## The Flooding Event

The flooding at the Burning Man site was caused by heavy rains, turning the desert into a mud-caked terrain that made it impossible for attendees to leave the festival site[^1^][^2^]. The unusual late-summer storm transformed the week-long counterculture fest into a sloppy mess with festival-goers stuck in foot-deep mud[^5^][^6^]. The roads became too wet to navigate, trapping over 70,000 attendees as the festival was coming to a close[^2^].

## Casualties and Investigations

Amidst the crisis, authorities were investigating a death at the site[^3^][^4^]. The details of the death investigation were not explicitly provided in the available information. However, it is clear that the flooding and subsequent stranding of attendees complicated the situation at the festival site.

## Response from the Burning Man Community

Despite the adverse conditions, the spirits of some Burning Man revelers reportedly remained unbroken[^5^][^6^]. The community response and efforts to deal with the crisis are not detailed in the provided information.

## Conclusion

The latest Burning Man festival was significantly affected by an unexpected natural disaster, leading to the stranding of thousands of participants and a death investigation. The event highlights the need for comprehensive emergency planning and preparedness in such large-scale events.

---

^1^ "No longer stranded, tens of thousands clean up and head home after..." AP News. 4 Sept. 2023. <https://apnews.com/article/burning-man-flooding-nevada-stranded-3971a523f4b993f8f35e158fd1a17a1e>.

^2^ "Officials investigate death at Burning Man as thousands stranded by floods." The Guardian. 3 Sept. 2023. <https://www.theguardian.com/culture/2023/sep/03/burning-man-nevada-festival-floods>.

^3^ "Death at Burning Man investigated in US, thousands stranded by flooding..." Al Jazeera. 3 Sept. 2023. <https://www.aljazeera.com/news/2023/9/3/death-under-investigation-after-storm-flooding-at-burning-man-festival>.

^4^ "Burning Man flooding strands tens of thousands as authorities investigate one death." France 24. 4 Sept. 2023. <https://www.france24.com/en/americas/20230904-burning-man-flooding-strands-tens-of-thousands-as-authorities-investigate-one-death>.

^5^ "Burning Man flooding strands tens of thousands at Nevada site; authorities are investigating 1 death." Inquirer. 3 Sept. 2023. <https://www.inquirer.com/news/nation-world/burning-man-flooding-nevada-death-investigation-20230903.html>.
