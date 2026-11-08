# All text and image choices for the site live here.
# Edit this file, then run:  python3 _build/build.py

SITE = {
    "name": "Bastian Fynboe",
    "title": "Bastian Fynboe — Brand & visual identity designer",
    "description": "Bastian Fynboe is a brand and visual identity designer based in Copenhagen.",
    "email": "bastianfynboe@gmail.com",
    "phone": "+45 51 51 41 24",
    "url": "https://bastianfynboe.xyz",
}

INTRO = {
        "hello": "Hi, I'm Bastian.",
    "text": "I'm a brand and visual identity designer in Copenhagen. Before that I spent years in film and TV, so I care a lot about the story.",
    "facts": [
        ("Now", "Open to junior roles and freelance identity work"),
        ("Education", "KEA, Entrepreneurship &amp; Design, 2024–2026"),
        ("Before", "Production coordinator in Danish film &amp; TV"),
    ],
}

PROJECTS = [
    {
        "slug": "vakkerbo",
        "title": "Vakkerbo",
        "client": "Vakkerbo",
        "year": "2026",
        "kind": "Visual identity, website, photography",
        "cover": "vk-cover",
        "lead": "Identity, website and product photography for Vakkerbo, a new Danish studio for interior design, art and vintage.",
        "meta": [
            ("Client", "Vakkerbo"),
            ("Year", "2026"),
            ("Services", "Visual identity, custom Shopify theme, logo animation, product photography"),
            ("Live", '<a href="https://vakkerbo.dk" target="_blank" rel="noopener">vakkerbo.dk</a>'),
        ],
        "blocks": [
            ("text", "The brief", "Vakkerbo is a new chapter from the founder of OYOY Living Design: interior design for homes and businesses, and a shop with one-off art and vintage pieces. It needed an identity and a website that felt calm and personal, with room for the objects to speak."),
            ("full", "vk-site", "The front page of vakkerbo.dk. The wordmark sits over a looping film of the founder's home."),
            ("text", "The website", "I built the site as a custom Shopify theme. As you scroll, the large wordmark shrinks and settles into the header, and the menu fades in. The site runs in Danish and English, and the shop sells unique pieces, one of each."),
            ("videos", ["vk-horse"], "The hand-drawn horse, animated for the site."),
            ("full", "vk-logo", None),
            ("text", "Photography", "I shot and edited the product photography for the shop: soft daylight, white lace and the pieces on their own."),
            ("trio", ["vk-2", "vk-3", "vk-4"], None),
            ("trio", ["vk-5", "vk-6", "vk-8"], None),
            ("full", "vk-room", "A still from the film on the front page."),
        ],
    },
    {
        "slug": "flok",
        "title": "FLOK",
        "client": "FLOK",
        "year": "2024",
        "kind": "Branding, concept development",
        "cover": "flok-cover",
        "lead": "A brand identity for FLOK, a community concept built on creativity, togetherness and collaboration.",
        "meta": [
            ("Client", "FLOK"),
            ("Context", "1st semester exam, KEA"),
            ("Services", "Branding, visual identity, concept development"),
            ("Methods", "Surveys, interviews, observations, the four design principles"),
        ],
        "blocks": [
            ("text", "The brief", "The challenge was to capture FLOK's sense of togetherness in an identity that stands out on a busy street. A flock of swallows became the core idea: birds sitting on the letters, hand-drawn type and posters that invite people to come and eat together."),
            ("full", "flok-logo", None),
            ("pair", ["flok-poster", "flok-pillar"], "Poster for the shared dinners, and out on the street."),
            ("full", "flok-swallow", "Sticker."),
            ("full", "flok-glued", None),
            ("full", "flok-window", None),
        ],
    },
    {
        "slug": "munkholm",
        "title": "Munkholm",
        "client": "Munkholm",
        "year": "2025",
        "kind": "Visual identity, packaging",
        "cover": "mh-cover",
        "lead": "A modernised identity for Munkholm, a Danish soap and skincare brand. The goal was to make it relevant to today's market while respecting its heritage.",
        "meta": [
            ("Client", "Munkholm"),
            ("Context", "2nd semester exam, KEA"),
            ("Services", "Visual identity, branding, packaging concepts"),
            ("Methods", "The four design principles: contrast, repetition, alignment, proximity"),
        ],
        "blocks": [
            ("text", "The brief", "Munkholm stands for quality, sustainability and simplicity, but the visual expression had fallen behind. I built the new identity on a quiet, high-contrast serif wordmark, a warm apricot colour and labels that say plainly what is inside."),
            ("full", "mh-logo", None),
            ("pair", ["mh-bottle", "mh-jar"], "Hand wash and foot balm."),
            ("full", "mh-label", "The final label."),
            ("full", "mh-dots", "An earlier, louder direction I tested and set aside."),
            ("full", "mh-card", None),
        ],
    },
    {
        "slug": "made-to-play-longer",
        "title": "Made to Play Longer",
        "client": "Palmes Tennis Society",
        "year": "2026",
        "kind": "Brand strategy, visual direction",
        "cover": "mtpl-tags",
        "lead": "A way for Palmes to talk about sustainability without pretending to be something it is not. Fewer pieces, better materials, and facts instead of green symbols.",
        "meta": [
            ("Client", "Palmes Tennis Society"),
            ("Context", "Final exam project, KEA 2026"),
            ("Services", "Brand analysis, concept, visual direction"),
            ("Methods", "Design thinking, Aaker, SWOT, interviews, survey"),
        ],
        "blocks": [
            ("text", "The brief", "Palmes is a Copenhagen tennis brand with a strong universe: red clay, court lines and a love of the game. Sustainability was never part of the story. As the founder put it in our interview, it simply wasn't what Palmes was built around. The question was how Palmes could take responsibility in a way that felt true to the brand, instead of bolting on a green layer."),
            ("text", "What I found", "I analysed how Aiayu, GANNI and Fichi communicate sustainability, and combined it with a survey and interviews with people in the target group. Everything pointed the same way. To be believed, the message has to be simple, documentable and rooted in the brand's own identity."),
            ("full", "mtpl-tag-detail", "Each piece is numbered. The back of the tag links to the story of the material."),
            ("text", "The concept", "Made to Play Longer turns limits into the story. Each piece is made in a small, numbered run, often from deadstock fabric left over from earlier production. 140 pieces, because that is how much fabric there was. The tone is concrete and a little dry: “We're not there yet. But here is what we do.”"),
            ("full", "mtpl-moodboard", "Visual direction: navy, court green and a single clay accent. No leaves, no globes."),
        ],
    },
    {
        "slug": "folkets-droemme",
        "title": "Folkets Drømme",
        "client": "KEA / 48 Timer Festival",
        "year": "2025",
        "kind": "Concept, installation design",
        "cover": "fd-tree",
        "lead": "An interactive installation in Folkets Park on Nørrebro that invited locals and visitors to share their dreams for the future.",
        "meta": [
            ("Client", "KEA / 48 Timer Festival"),
            ("Context", "Team project, 48 Hours Festival"),
            ("Services", "Concept development, visual identity, installation design"),
            ("Methods", "Surveys, interviews, observations"),
        ],
        "blocks": [
            ("text", "The idea", "As part of the 48 Hours Festival, my team created “Folkets Drømme”. People wrote down their dreams and wishes, and we collected them in a large installation inspired by dreamcatchers, hung in the trees of the park. I worked on the concept and the visual identity, including the posters that called people in."),
            ("pair", ["fd-poster", "fd-single"], "The poster, and on a wall on Nørrebro."),
            ("full", "fd-cover", None),
        ],
    },
    {
        "slug": "selected-work",
        "title": "Selected work",
        "client": "School &amp; self-initiated",
        "year": "2024–2026",
        "kind": "Editorial, posters, motion",
        "cover": "sel-loop-1",
        "lead": "Smaller projects from an intensive graphic design course, and things I make on my own.",
        "meta": [
            ("Context", "Graphic design course, KEA, and personal projects"),
            ("Tools", "InDesign, Illustrator, Photoshop, After Effects, Blender"),
        ],
        "blocks": [
            ("pair", ["sel-loop-1", "sel-loop-2"], "LOOP, design manual."),
            ("pair", ["sel-venus", "sel-poster"], "Typographic posters."),
            ("videos", ["glyptoteket", "dovely"], "3D logo study for Glyptoteket, and a logo animation."),
            ("full", "sel-horses", "Image experiment."),
        ],
    },
]

ABOUT = {
    "body": [
        "Since I was a small boy, I've been drawn to stories and visuals. Growing up in Western Jutland, I spent countless hours watching films with my grandparents on old VHS tapes. That led me to Ebeltoft Film Folk High School, and later to the film industry in Copenhagen, where I worked my way up from runner to production coordinator and 1st AD. It taught me to stay organised, creative and calm under pressure.",
        "But film wasn't the full picture for me. In 2024 I started Entrepreneurship &amp; Design at KEA and stumbled into graphic design. My very first project was a poster for a made-up event on Christianshavn. I had just downloaded Adobe and had never designed anything. I would change a lot about it today, but from that moment on I was hooked.",
        "I don't see myself as a finished designer, and I hope I never will. For me, design is about learning, experimenting and pushing myself, and about combining my film background, my roots and my love of visuals into something that feels both personal and professional.",
    ],
    "lists": [
        ("Experience", [
            "Production coordinator / 1st AD, Thin Green Line Productions, 2022–",
            "TV productions for DR, incl. Store Danske Kunstnere",
        ]),
        ("Education", [
            "KEA, Entrepreneurship &amp; Design, 2024–2026",
            "European Film College, Ebeltoft, 2020–2021",
            "Lycée du Val d'Argens, France, 2017–2018",
        ]),
        ("Skills", [
            "Brand &amp; visual identity",
            "Illustrator, InDesign, Photoshop, After Effects, Figma",
            "Web design &amp; Shopify",
            "Concept development &amp; design thinking",
        ]),
    ],
}
