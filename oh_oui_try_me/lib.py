import random


def try_me():
    acronyme = [
        "A-level ou A+ : Les abréviations en A désignent souvent l’anal. A-level ou A+ sont les plus courantes. En général cette abréviation est accompagné du terme « extra » désignant le surplus financier pour cette pratique.",
        "ATM : Ass to mouth. Le ATM est le fait de passer de l’anus de l’escort à sa bouche. Certains trouvent ça dégoûtant, d’autres adorent. C’est assez rarement pratiqué et quand ça l’est ça signifie, évidemment, que l’escort accepte l’anal.",
        "BBJ ou BBBJ : Bareback Blowjob. En anglais Bareback signifie monter à cheval sans selle. Pour le sexe Bareback désigne l’absence de préservatif. Le Bareback blowjob est donc la fellation sans préservatif. On ne pourra que vous conseiller d’éviter ce genre de pratiques, les escorts n’étant pas le métier le moins exposé aux MST.",
        "BBFS : Bareback sex. Le bareback sex est le sexe sans préservatif. Cf ci-dessus.",
        "BBBJTC : bare back blow job to completion . Le BBBJTC est la fellation sans préservatif jusqu’à l’orgasme. VOus trouverez parfois le BBBJTCIM qui est la fellation sans préservatif, jusqu’à l’orgasme et avec éjaculation dans la bouche. (bare back blow job to completion in mouth)",
        "BBJTCNQNS : bare back blow job to completion, no quit, no spit. Le BBJTCNQNS est l’abréviation la plus longue dans le milieu de la prostitution et peut être même la plus longue au monde (évitez quand même de briller avec cette info dans vos repas de famille). Elle désigne le fait de pratiquer une fellation sans préservatif et de rester jusqu’à l’orgasme sans retirer sa bouche.",
        "BBBJWF : bare back blow job with facial. C’est comme la BBBJTCIM sauf que ça se termine par une éjaculation faciale.",
        "BBBJTCWS : bare back blow job to completion with swallow. Comme le BBBJTCIM et le BBBJWF mais avec un swallow à la fin. Un swallow c’est le fait de garder en bouche l’éjaculation. On aime ou on déteste.",
        "BLS : Ball Licking and Sucking. C’est assez transparent pour quiconque a fait plus d’une année d’anglais. C’est le fait de lécher et sucer les testicules.",
        "BS : BodySlide. Le BS n’est ni plus ni moins qu’un massage. Vous êtes dans le milieu de la prostitution, il y a donc de grande chance qu’il s’agisse soit de préliminaires soit de massage avec finition.",
        "CBJ : Covered Blowjob. Le CBJ est la fellation avec préservatif. Pas la meilleure niveau sensation mais avec une prostituée elle est de loin la plus prudente.",
        "CDS : Covered Doggystyle. Levrette avec préservatif. Rarement précisé mais il arrive de tomber sur cette abréviation",
        "CIF : Cum in Face. Le petit nom de l’éjaculation faciale, l’une des abréviations les plus utilisées avec le CIM et le COB.",
        "CIM : Cum in Mouth. C’est l’éjaculation faciale.",
        "COB : Cum on body ou Cum on breast. Les 2 termes ne veulent pas dire exactement la même chose mais sont quand même assez proches. Ils décrivent l’éjaculation sur le corps ou sur les seins. Les seins faisant partie du corps on arrive souvent au même résultat.",
        "DATO : Dining at the 0. DATO est une abréviation poétique désignant l’anulingus. Dining pour manger, le « o » pour vous voyez bien quoi.",
        "DATY : Dining at the Y. Rien à voir avec Rachida. Daty désigne le cunnilingus.",
        "DDP : Double Digit Penetration. La DDP est la pratique désignant la double pénétration vaginale et anale avec vos doigts.",
        "DFK : Le Deep French Kiss est un baiser sur la bouche très appuyé. Il est souvent l’appanage des escort GFE.",
        "DIY : Do it Yourself. C’est très clair, Do It Yourself signifie « fais le toi même » et désigne la masturbation. Vous avez le droit de payer une escort DIY mais seulement si vous avez beaucoup trop d’argent sur votre compte. Sinon c’est un peu du gâchis.",
        "DP : Dans le porno comme dans la prostitution, la DP est la double pénétration. Bien sûr pour faire une DP il faut être 2. Ou avoir grandi trop prêt d’un réacteur nucléaire.",
        "DT : Le terme Deepthroat est très utilisé dans le porno et ce depuis l’un des tous premiers porno. Il désigne la « gorge profonde », la fellation où l’escort prend en entier le membre de son client.",
        "FBSM : Full body sensual massage. Le massage sensuel sur tout le corps est un massage érotique pouvant être avec ou sans finition. Il sera sans finition presque uniquement s’il est pratiqué comme préliminaire",
        "FK : On a vu le DFK plus haut, le FK est le french kiss pas spécialement appuyé.",
        "GFE : Girlfriend experience. La girlfriend experience est pratiquée par les escorts se comportant comme votre petite amie. Leur sexualité sera plutôt douce, elles vous embrasseront, vous calineront, prendront soin de vous après l’orgasme… par opposition à la PSE.",
        "GSM : G-Spot massage. Le G-spot c’est le point G. Chez les hommes il est situé dans la prostate. Le seul moyen d’y accéder c’est par l’anus. Le G-spot massage est donc le massage du point G.",
        "HJ : Handjob. Ce terme désigne la masturbation. Prendre un escort pour un HJ c’est vraiment du luxe.",
        "MSOG : Le Multiple shot on goal est l’une des prestations les plus intéressante. Une escort qui mentionne MSOG vous permettra d’avoir autant de rapports que vous voulez pendant le temps que vous aurez réservé. Une pratique très commerçante qui honore celles qui l’offrent.",
        "OWO : Oral without condom. Identique au BBBJ, c’est la fellation sans préservatif.",
        "OWC : L’inverse de OWO, elle désigne l’oral with condom, la fellation protégée.",
        "PSE : La PSE est la pornstar experience. Elle est mentionnée pour les escort qui se vantent de vous faire vivre un vrai film porno avec elles. Pour une vraie PSE il faudra un minimum de sentiments, des pratiques un peu extrêmes et un peu vulgaire. L’inverse de la GFE.",
        "RPG : Role Playing Game. On connaît le terme RPG dans le monde des jeux vidéo. Dans la prostitution le RPG est un jeu de rôle coquin où l’escort jouera le rôle qui collera le plus à vos fantasmes.",
        "SOG : précédé d’un chiffre, SOG (shot on goal) signifie que vous aurez le droit à x rapports. Vous ne paierez alors pas au temps mais au nombre de rapports.",
        "SOMF : Sat on my face. Le face sitting est assez à la mode depuis quelques temps et est désigné soit par l’abréviation SOMF soit par son nom complet.",
        "TG : TransGender. C’est assez transparent. TG signifie que vous avez affaire à un transsexuel.",
        "TUMA : Tongue up my ass. Synonyme de rimming ou de rimjob, TUMA désigne l’anulingus.",
        "TV : Transvestite. Un TV est un travesti."
    ]
    i = random.randint(0, len(acronyme)-1)
    return(acronyme[i])
