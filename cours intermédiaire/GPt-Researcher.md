
# Moteur de recherche [Tavily](https://docs.tavily.com/docs/examples/examples)

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

# [Gpt Research](https://github.com/assafelovic/gpt-researcher?tab=readme-ov-file)
- Complément de code:
```Python
from gpt_researcher import GPTResearcher
import asyncio

# It is best to define global constants at the top of your script
QUERY = "What happened in the latest burning man floods?"
REPORT_TYPE = "research_report"

async def fetch_report(query, report_type):
    """
    Fetch a research report based on the provided query and report type.
    """
    researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
    report = await researcher.run()
    return report

async def generate_research_report():
    """
    This is a sample script that executes an async main function to run a research report.
    """
    report = await fetch_report(QUERY, REPORT_TYPE)
    print(report)

if __name__ == "__main__":
    asyncio.run(generate_research_report())
```
- Résultat:
# In-Depth Report on the 2023 Burning Man Floods
## Introduction


The Burning Man festival, an annual event known for its celebration of community, art, and self-expression, faced an unprecedented challenge in 2023. Torrential rains and flooding transformed the Black Rock Desert in Nevada, typically a dry and dusty expanse, into a muddy quagmire, significantly impacting the festival and its attendees. This report delves into the events that unfolded, the response from organizers and authorities, and the broader implications of such extreme weather events.


## The Onset of the Storm


The festival, which began on August 28, 2023, was initially met with typical conditions for the desert environment. However, the weather took a dramatic turn as remnants of Hurricane Hilary, downgraded to a tropical storm by the time it reached the area, brought heavy rainfall to the region. The Black Rock Desert received approximately 0.8 inches of rain in just 24 hours between Friday and Saturday morning, which is about twice the average rainfall for the entire month of September (CNN, 2023).


## Impact on the Festival


The rain had a significant impact on the festival's infrastructure and logistics. The playa, the desert basin where the event is held, became impassable due to the mud, leading to a halt in vehicle traffic. Organizers were forced to issue a "shelter in place" directive and advised attendees to conserve food and water. Entry and exit from the area were suspended, leaving many of the 70,000 participants stranded (NBC News, 2023).


Despite the conditions, the festival's centerpiece event, the burning of the Man, took place one day later than scheduled. However, the aftermath of the storm left the organizers with the enormous task of adhering to the "Leave No Trace" policy, a stipulation of their permit that requires the land to be left as it was found. This meant not only picking up trash but also recontouring the playa to smooth out all the tracks left by vehicles (NPR, 2023).


## Response and Recovery Efforts


The festival's organizers, along with local, county, state, tribal, and federal agencies, coordinated a response to the weather conditions. They provided a "2023 Wet Playa Survival Guide" to assist attendees and set up mobile cell service and charging stations around the festival grounds. Shuttle buses were also deployed to help with the exodus once conditions improved (ABC News, 2023).


President Joe Biden was briefed on the situation, and the White House stated that administration officials were monitoring the event and receiving updates from state and local officials. The White House urged attendees to heed updates from these officials and the event organizers (NBC News, 2023).


## Health and Safety Concerns


The flooding raised concerns about the health and safety of the attendees. Volunteer medics were particularly worried about hypothermia, waste exposure, and dehydration. Despite these concerns, the community spirit of Burning Man shone through, with many attendees offering shelter and resources to those in need (NBC News, 2023).


## Environmental and Climate Implications


The flooding at Burning Man has been cited as a "teachable moment" about climate change. While no single storm can be directly attributed to climate change, Nevada state officials have warned that such flooding is expected to become more frequent as storms intensify and snow shifts to rain due to higher temperatures. This event has fueled criticism of the festival's environmental footprint, as the rush to leave the encampment resulted in more trash being left behind than usual (The Washington Post, 2023).


## Aftermath and Public Reaction


As the roads dried and the driving ban was lifted, attendees began their mass exodus from the site. The situation was exacerbated by the fact that many festivalgoers were unprepared for the cold and wet conditions, leading to a challenging departure. Social media was flooded with both sympathetic and critical reactions, with some expressing concern for the attendees' well-being and others making light of the situation (The Guardian, 2023).


## Conclusion


The 2023 Burning Man festival was a stark reminder of the unpredictability of nature and the importance of preparedness for extreme weather events. The response from the Burning Man community and the coordinated efforts of various agencies demonstrated resilience in the face of adversity. However, the incident also highlighted the need for greater environmental awareness and adaptation strategies as the frequency and intensity of such events are likely to increase in a changing climate.


## References


- CNN. (2023). Burning Man attendees make a mass exodus after a dramatic weekend that left thousands stuck in the Nevada desert. https://edition.cnn.com/2023/09/05/us/burning-man-storms-shelter-exodus-tuesday/index.html

- NBC News. (2023). Live updates: Burning Man flooding keeps thousands stranded at Nevada site. https://www.nbcnews.com/news/us-news/live-blog/live-updates-burning-man-flooding-keeps-thousands-stranded-nevada-site-rcna103193

- ABC News. (2023). Burning Man flooding: What happened to stranded festivalgoers? https://abcnews.go.com/US/burning-man-flooding-happened-stranded-festivalgoers/story?id=102908331

- The Washington Post. (2023). Burning Man exodus flooding climate change. https://www.washingtonpost.com/climate-environment/2023/09/05/burning-man-exodus-flooding-climate-change/

- NPR. (2023). Burning Man climate change activists. https://www.npr.org/2023/09/07/1198054587/burning-man-climate-change-activists

