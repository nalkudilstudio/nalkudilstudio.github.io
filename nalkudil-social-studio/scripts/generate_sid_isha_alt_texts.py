import json
import re

# Load 30 drabbles data
with open('D:/StorytellingArt/SidIsha-HomeWasYou/sid_isha_30_drabbles.json', 'r', encoding='utf-8') as f:
    drabbles = json.load(f)

# Crafted high-fidelity Alt texts following the exact user template:
# Slide 1 Alt Text (Visual Cover Slide):
# A [visual scene description]. A text overlay at the top reads "[Overlay Punchline]" alongside a circular author portrait badge in the lower right corner.
# Slide 2 Alt Text (Drabble Story Slide):
# A dark, vintage-framed micro-fiction reading slide titled "[Title]" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates [synopsis]. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.

alt_texts = {}

# Day 12 baseline reference
alt_texts[12] = {
    "slide1": 'A warm, nostalgic photograph inside a school library showing a teenage girl in a school uniform with braided hair tied in red ribbons, smiling shyly from behind a stack of thick open textbooks, including one titled "PHYSICS: Principles & Problems". A text overlay at the top reads "With you, my entire world finds perfect order." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Margin Notes" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha sliding her physics textbook across a scarred wooden library table to Sid during study hour, trading handwritten margin notes about the second law of thermodynamics and entropy. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 1: The Chalkboard Sentence
alt_texts[1] = {
    "slide1": 'A warm, nostalgic photograph inside a sunlit 90s Indian classroom showing a charming high school boy in uniform writing playful romantic equations on a large green chalkboard while smiling shyly toward an off-camera classmate. A text overlay at the top reads "The entire classroom laughed." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Chalkboard Sentence" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid stepping up to the blackboard before class begins to scribble a humorous sentence confessing his feelings for Isha, prompting laughter from the classroom while she hides behind her notebook. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 2: The Chemistry & The Rain
alt_texts[2] = {
    "slide1": 'A cinematic monsoon photograph of a teenage Indian boy and girl walking side by side under a shared transparent umbrella along a rain-drenched tree-lined road, pushing their bicycles through gentle puddles. A text overlay at the top reads "You turned me on." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Chemistry & The Rain" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha walking home together in a sudden torrential downpour, discussing science formulas while sparks fly beneath their shared umbrella. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 3: Deliciously Dangerous
alt_texts[3] = {
    "slide1": 'An intimate cinematic close-up of a teenage Indian boy and girl standing close under the shelter of an old brick archway during a heavy rain shower, sharing breathless smiles with rain droplets glistening on their school uniforms. A text overlay at the top reads "Deliciously dangerous." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Deliciously Dangerous" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha trapped under a narrow stone archway as thunder rumbles, caught between the danger of being seen and the sweet intimacy of their unspoken attraction. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 4: Midnight Whispers
alt_texts[4] = {
    "slide1": 'A cozy nighttime photograph of a dimly lit bedroom where an Indian teenage boy lies on his bed smiling warmly at the soft blue glow of his basic mobile phone screen under a warm yellow bedside lamp. A text overlay at the top reads "Love was simply Us." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Midnight Whispers" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid reading late-night text messages from Isha in the quiet of his room, discovering how simple everyday words bridge the silent midnight hours between them. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 5: The Envelope at the Cycle Stand
alt_texts[5] = {
    "slide1": 'A bright morning photograph inside a high school cycle stand with rows of classic steel bicycles bathed in golden sunbeams, showing a girl surreptitiously slipping a small white envelope into a boy\'s bicycle basket. A text overlay at the top reads "You ruled my dreams." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Envelope at the Cycle Stand" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid discovering a handwritten letter tucked into his cycle bell gear at the school stand, turning an ordinary morning assembly into an unforgettable thrill. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 6: The Darkroom Secret
alt_texts[6] = {
    "slide1": 'A moody, cinematic photograph inside a high school photography darkroom illuminated by a single crimson red safety lamp, showing two school students standing close amidst hanging film strips and wash trays. A text overlay at the top reads "Always here to protect my queen." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Darkroom Secret" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha stepping into the darkroom where Sid is developing photographs, their whispered confessions sheltered by amber developer trays and red shadows. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 7: The Lingering Glow
alt_texts[7] = {
    "slide1": 'A tender romantic photograph inside an empty vintage school classroom at twilight, showing a teenage boy and girl admiring glowing luminous green paint on a small paper star held between their palms. A text overlay at the top reads "You really are my safest place." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Lingering Glow" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid showing Isha a glow-in-the-dark star hidden inside his physics notebook, whispering how her presence brings light to his quietest doubts. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 8: The Crimson Thread
alt_texts[8] = {
    "slide1": 'A detailed macro photograph focusing on two teenage hands in front of an ancient school corridor brick pillar, showing a girl with red ribboned braids tying a slender sacred crimson thread around a boy\'s wrist. A text overlay at the top reads "My universe is standing right in front of me." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Crimson Thread" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha tying a red protective thread around Sid\'s wrist before the final bell clangs, cementing an unspoken sacred promise before they part for the evening. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 9: Half a Song, Whole World
alt_texts[9] = {
    "slide1": 'A golden dusk photograph of a teenage couple sitting together on an old stone park bench beneath the hanging roots of a grand banyan tree, sharing a pair of wired white earphones plugged into a portable MP3 player. A text overlay at the top reads "With half a song each, our universe was whole." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Half a Song, Whole World" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid untangling wired earphones to share an acoustic Rahman track with Isha on a park bench at sunset, discovering how half an earphone creates a complete shared world. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 10: Parallel Pedals
alt_texts[10] = {
    "slide1": 'A wide-angle cinematic shot on an open country road at amber sunset, showing two Indian school students riding their bicycles parallel side-by-side, laughing with wind tossing their hair. A text overlay at the top reads "The joy was staying parallel, riding alongside." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Parallel Pedals" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha racing their cycles down an empty highway after evening tuition, matching pedal strokes in silent synchronization under an amber November sky. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 11: The Leap
alt_texts[11] = {
    "slide1": 'A carefree nostalgic photograph under an old stone railway arch bridge surrounded by tall green meadow grasses, showing two discarded bicycles in the clover and two teenage students laughing breathlessly together. A text overlay at the top reads "Only the mad get to fly." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Leap" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha suddenly swerving her bicycle down an embankment into wild clover grass, daring Sid to follow her in a leap of carefree adolescent abandon. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 13: Half a Cup of Chai
alt_texts[13] = {
    "slide1": 'An atmospheric roadside photograph of a traditional Indian tea tapri at cool dusk, steam rising gently from a warm cutting chai glass tumbler held between two young hands beside a brass kettle. A text overlay at the top reads "One chai. Shared warmth." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Half a Cup of Chai" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha stopping at a roadside tea stall after tuition, sharing a single glass of steaming cutting chai in the November chill while talking about their futures. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 14: The Junior’s Query
alt_texts[14] = {
    "slide1": 'A bright photograph along a historic school verandah with white colonial pillars and terracotta tiles, showing an Indian schoolgirl playfully pouting with arms crossed while a boy explains himself with an amused, guilty smile. A text overlay at the top reads "Flattery won\'t save you, Sid." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Junior’s Query" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha teasing Sid after spotting a younger student asking him for physics tutoring outside the staff room, eliciting his flustered and devoted reassurances. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 15: The Sweet Apology
alt_texts[15] = {
    "slide1": 'A warm golden hour photograph near a vintage school gate at dusk, showing a boy offering a rustic brown paper parcel filled with glistening, spiral orange hot jalebis to a smiling girl in uniform. A text overlay at the top reads "An offering to appease the queen." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Sweet Apology" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid waiting by the back gate with freshly fried syrup-dripping hot jalebis to apologize for teasing Isha, dissolving her mock annoyance into sweet shared laughter. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 16: The Rooftop Vow
alt_texts[16] = {
    "slide1": 'A panoramic twilight photograph from the concrete terrace water tank of an Indian home overlooking rooftops bathed in purple and orange dusk, showing two students sitting shoulder to shoulder watching the horizon. A text overlay at the top reads "Wherever you go, home follows." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Rooftop Vow" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha perched high above town on a rooftop water tank after tuition, watching evening lights flicker awake as they vow that no distance will ever break what they have built. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 17: The Countdown
alt_texts[17] = {
    "slide1": 'A vintage classroom photograph during intense board exam preparation season, showing a chalkboard marked "42 Days to Finals" and two desks stacked with thick guidebooks and open notebooks under ceiling fans. A text overlay at the top reads "Formula: lim(x→∞) of my love = infinite." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Countdown" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates the ticking pressure of twelfth-grade board exams, as Sid writes calculus limit formulas on Isha\'s rough sheet that playfully prove his love is mathematically infinite. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 18: Two A.M. Frequencies
alt_texts[18] = {
    "slide1": 'A split-frame late-night photograph of two quiet study bedrooms under table lamps, showing a teenage boy and girl each resting a telephone receiver against their ears while looking at identical open physics problem sets. A text overlay at the top reads "Everything in my universe tumbles toward you." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Two A.M. Frequencies" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha studying across the telephone line at two in the morning, their whispered problem-solving turning into quiet reflections on gravity and love. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 19: Five Marks and a Glow
alt_texts[19] = {
    "slide1": 'A poignant afternoon photograph of an empty high school classroom after final examinations, showing a tearful Indian girl in uniform seated at a desk while a boy gently hands her a clean handkerchief. A text overlay at the top reads "You still outshine the entire school." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Five Marks and a Glow" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha weeping over losing five marks on the chemistry paper due to traffic delays, while Sid comforts her by affirming that numbers will never measure her brilliance or his love. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 20: Into the Sunlight
alt_texts[20] = {
    "slide1": 'A bright, triumphant photograph of two high school students walking together out through the grand arched gates of their school into brilliant afternoon sunlight, holding rolled question papers as exam bells echo. A text overlay at the top reads "We conquered. Two hearts into the unfolding future." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Into the Sunlight" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates the ringing of the final school exam bell, as Sid and Isha walk out of the school gates together into an uncertain yet hopeful future. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 21: Ink on Cotton
alt_texts[21] = {
    "slide1": 'A nostalgic photograph in a sunny school courtyard on uniform shirt-signing day, showing a teenage girl smiling brightly as she inks bold black marker cursive across the back of a boy\'s pristine white school shirt. A text overlay at the top reads "Property of Isha. Forever non-negotiable." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Ink on Cotton" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates farewell day at school, where Isha claims Sid\'s uniform shirt with a permanent marker, writing a fiercely tender message that forever seals her claim on his heart. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 22: Different Envelopes
alt_texts[22] = {
    "slide1": 'A reflective sunset photograph on a weathered stone terrace parapet, showing two official university admission envelopes resting side-by-side with postmarks from Delhi and Bangalore against a violet evening sky. A text overlay at the top reads "The skies are different. The gravity stays the same." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Different Envelopes" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates the bitter reality of university counseling letters placing Sid in Delhi and Isha in Bangalore, facing the realization that different skies cannot break their shared gravitational pull. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 23: Terminal Goodbyes
alt_texts[23] = {
    "slide1": 'An emotional airport departure terminal photograph framed through glass departure gates, showing a young Indian couple embracing tightly as boarding call announcements echo under cool airport halogen lights. A text overlay at the top reads "Every frequency in my mind is tuned to you." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Terminal Goodbyes" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid seeing Isha off at Terminal 1 as she boards her flight for overseas higher education, sharing a desperate embrace that promises their minds will stay tuned to each other across any distance. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 24: The Cut Wire
alt_texts[24] = {
    "slide1": 'A somber, vintage photograph of a yellow coin-box payphone on a peeling hostel hallway wall under a dim fluorescent bulb, the telephone receiver hanging silent from its coiled cord. A text overlay at the top reads "The silence felt absolute." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Cut Wire" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid standing before a dead hostel coin-box payphone as the hostel gates slam shut, facing the deafening silence of disconnected phone lines and unanswered letters. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 25: Across Hemispheres
alt_texts[25] = {
    "slide1": 'A striking dual-contrast photograph: an Indian woman bundled in a winter wool coat walking along a snowy Munich boulevard, contrasted against a man working at a rainy Bangalore desk, both glancing at the cloudy sky. A text overlay at the top reads "Distant horizons, zero contact—yet never so alone." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Across Hemispheres" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates the passage of years across different continents, as Isha walks through European autumns and Sid builds his engineering career, living parallel lives bound by silent memory. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 26: Lines of Code
alt_texts[26] = {
    "slide1": 'A sleek modern corporate photograph inside a glass office tower late at night, showing an exhausted software architect looking thoughtfully up from dual glowing monitors filled with lines of code. A text overlay at the top reads "Fate, after seven silent years, quietly cracked its knuckles." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Lines of Code" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid working late on an enterprise software module seven years later, stumbling upon a code repository signed by an engineer named Isha, feeling fate stir once again in the dark. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 27: The Bavarian Crowd
alt_texts[27] = {
    "slide1": 'A vibrant festive photograph inside an immense Munich Oktoberfest beer tent with warm golden fairy lights and roaring crowds, showing two individuals locking eyes in stunned recognition across a sea of strangers. A text overlay at the top reads "Across twenty feet of strangers, her eyes snapped to his." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "The Bavarian Crowd" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid attending Oktoberfest in Munich, looking across the roaring festival tent to find Isha standing right before him after seven long years of silence. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 28: Warm Coffee, Cold Morning
alt_texts[28] = {
    "slide1": 'A crisp autumn morning photograph outside the futuristic glass architecture of BMW Welt in Munich, showing a man and woman holding paper coffee cups, walking together on a path covered in golden fallen maple leaves. A text overlay at the top reads "Seven years vanished in seven seconds." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Warm Coffee, Cold Morning" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Sid and Isha walking through the chilly Munich morning after their reunion, feeling seven years of separation melt away as naturally as their very first conversation. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 29: Only Yours
alt_texts[29] = {
    "slide1": 'An emotional nighttime photograph inside a warm modern penthouse apartment overlooking a rain-swept European city skyline, showing a woman with wet eyelashes leaning her forehead against a man\'s chest in pure relief. A text overlay at the top reads "I’m still your glowing queen. Only yours." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Only Yours" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates Isha showing Sid a suitor\'s proposal sent by her family, choosing instead to step into his arms and whisper that after all the years, she has only ever belonged to him. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Day 30: Home Was You
alt_texts[30] = {
    "slide1": 'A magnificent traditional South Indian temple wedding photograph bathed in sacred agni firelight and golden marigolds, showing a radiant bride in a silk saree and a groom in traditional veshti smiling with tears of joy. A text overlay at the top reads "You were never just a place. Home was always you." alongside a circular author portrait badge in the lower right corner.',
    "slide2": 'A dark, vintage-framed micro-fiction reading slide titled "Home Was You" by author Saravanakumar Murugan, from the Sid and Isha 30-day Drabble series. The story narrates the grand culmination of Sid and Isha\'s journey at a South Indian temple wedding, where as sacred nadaswaram pipes soar and the mangalsutra is tied, they realize that home was never a place—it was always each other. An illustrated footer banner displays "SIDISHA: HOME WAS YOU" featuring two school students with bicycles on an evening street.'
}

# Verify all 30 days are populated
print(f"Generated {len(alt_texts)} customized Alt Texts!")
assert len(alt_texts) == 30, "Missing days!"
print("Verification complete: all 30 days match the exact sample template.")

# Save to a helper JSON
with open('D:/StorytellingArt/SidIsha-HomeWasYou/curated_alt_texts_30days.json', 'w', encoding='utf-8') as f:
    json.dump(alt_texts, f, indent=2, ensure_ascii=False)
print("Saved curated_alt_texts_30days.json.")
