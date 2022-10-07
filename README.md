# The NUFORC Vitrine

<p align="center">
	<a href="https://nuforc.org/">
    		<img src="https://www.archives.gov/files/topics/ufo-banner2.gif" width="750" height="300"/>
	</a>
</p>

---

## Overview

This repository stores my data obtention methods, as well as the (nearly finished) Tableau workbook showcasing my analysis and insights.

---

## Briefing

All data was collected, cleaned, analysed and visualised by me.


### Data cleansing
I found [Kiru](https://github.com/kiru)'s [take on the matter](https://github.com/kiru/ada_project) too involved. I achieved a near-identical result to Kiru with a more modest approach — that is without parallelisation, by indexing the database by date rather than shape (unsure why this choice was made), using a quarter of the dependencies, and in far fewer lines.

Most fields are treated as freetext fields, and clearly no validation occured at the point of data entry:
1.	`Duration` is given textually (e.g. "1 second", "3 minutes") and is heavily strewn with mistakes, confused entries, and then just absolute poppycock. Syntactic analysis on this is extremely difficult.
2.	`Time` has sporadic "-1" entries.
3.	`Shape` is also clearly freetext, though after correcting spelling mistakes and capitalisation it boils down to only about 25 categories, thankfully. Many of these are similar enough though, so I've combined and renamed the categories down to 15.
4.  `Comment` text is encoded horrifically.
5.	`Country` is a mess:
	-	Nonsense entries include but are not limited to:
	    * "4 miles at sea"
		* "?!?!"
		* "dont know"
		* "military report"
		* "jacksonveil"
		* "ingerland!"
		* "between; mountain top"
	-	Misnomers and reduplicates (many due to the database's age):
		  * all Canadian locations are labelled as American — that's ~96% of the dataset obsolete since we can't discern the two.
		* "Papua/New Guinea"
		* "Viet Nam"
		* "U.K." and "United Kingdom" and "United Kingdom uk"
		* "Trinidad/Tobago" and "Trinidad and Tobago" and "Trinidad & Tobago"
		* "Brasil"
		* Many "Republic of"s and "Rep. of"s
6.	`Latitude` and `Longitude` are completely missing for countries outside of the U.S. and Canada. Cannot speak to their veracity.

<br />
<br />
<br />

### Comments on the data
* California has experienced more UFO sightings than every country outside of the U.S. combined.
* Colouring is proportional to LOG(COUNT+1). Combined with a diverging palette, countries with a COUNT of 1 are made brown and the rest are on a seemingly separate, sequential palette.
* NUFORC website launched in June 2001.
* The U.S. Defense Intelligence Agency's Advanced Aerospace Threat Identification Program ran from 2007 to 2012. After its start we observe a marked increase in reporting, even compared to the boost from the website's launch. We also see a decline in reporting shortly after its termination.
* Three days of note: July 4th, February 29th, and November 7th.
  * 04/07 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I think this one's self-explanatory.
  * 29/02 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; While NUFORC vets all reports and ensures they're not pranks, this is probably exactly that.
  * 07/11 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ???
* Datetime entries with missing time are imputed at midnight on the dot. There were 3,062 missing entries and no original entries at 00:00:00 exactly. All 00:00:00 entries are therefore NaTs.
* A more thorough accounting can be found [here](https://ada-nuforc-analysis.github.io/), courtesy of [kiru](https://github.com/kiru).

---

## License

Everything here is [unlincensed](LICENSE).
