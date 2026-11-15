from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Eiichiro Oda (Japanese: 尾田 栄一郎, Hepburn: Oda Eiichirō; born January 1, 1975) is a Japanese manga artist and the creator of the series One Piece, the best-selling manga in history and the best-selling comic series printed in volume.[1] With more than 600 million tankōbon copies of One Piece in circulation worldwide, Oda is one of the best-selling fiction authors.[2] The series' popularity resulted in Oda being named one of the artists who changed the history of manga.

Early life
Eiichiro Oda was born on January 1, 1975, in Kumamoto, Japan. At the age of four he resolved to become a manga artist in order to avoid having to get a "real job".[3] His biggest influence was Akira Toriyama and his series Dragon Ball.[3][4] He recalls that his interest in pirates was probably sparked by the popular TV animation series titled Vicky the Viking.[5]

Career
At the age of 17, Oda submitted his work Wanted! and won several awards, including second place in the coveted Tezuka Award. That got him into a job at the Weekly Shōnen Jump magazine, where he originally worked as assistant manga artist/assistant to Shinobu Kaitani's series Suizan Police Gang before moving to Masaya Tokuhiro on Jungle King Tar-chan and Mizu no Tomodachi Kappaman,[3] which gave him an unexpected influence on his artistic style. At the age of 19, he began working as an assistant to Nobuhiro Watsuki on Rurouni Kenshin, before winning the Hop Step Award for new manga artists. Watsuki credits Oda for helping create the character Honjō Kamatari who appears in Rurouni Kenshin.[6]

During this time, Oda drew two pirate-themed one-shot stories called "Romance Dawn", which were published in Akamaru Jump and Weekly Shōnen Jump respectively in late 1996.[7][8] "Romance Dawn" featured Monkey D. Luffy as the protagonist, who then became the protagonist of One Piece.

In 1997, One Piece began serialization in Weekly Shōnen Jump and has become not only one of the most popular manga in Japan, but the best-selling manga series of all time. It sold 100 million collected tankōbon volumes by February 2005,[9] over 200 million by February 2011,[9] had 320,866,000 copies printed worldwide by December 2014,[10] 430 million volumes in circulation worldwide as of October 2017,[11] 440 million copies sold as of May 2018,[12] 450 million in print as of March 2019,[13] and 600 million in print as of March 2026.[14]

Additionally, individual volumes of One Piece have broken publishing records in Japan. Volume 56 received the highest initial print run of any manga, 2.85 million copies, in 2009.[15] Volume 57's print of 3 million in 2010 was the highest first print for any book in Japan, not just manga. A record that was broken several times by subsequent volumes and currently held by 67's 4.05 million initial printing in 2012.[16] In 2013, the series won the 41st Japan Cartoonists Association Award Grand Prize, alongside Kimuchi Yokoyama's Nekodarake Nice.[17]

In a 2008 poll, conducted by marketing research firm Oricon, Oda was elected fifth most favorite manga artists of Japan. He shared the place with Yoshihiro Togashi, creator of YuYu Hakusho and Hunter × Hunter.[18] In their 2010 poll on the Mangaka that Changed the History of Manga, Oda came in fourth.[19]

For the tenth One Piece animated theatrical film, Strong World, Oda created the film's story, drew over 120 drawings for guidance and insisted Mr. Children provide the theme song.[20][21] Additionally, a special chapter of the manga was created and included in tankōbon volume 0, which was given free to attendees of the film and also contained his drawings for the film.[22] Following the particular success of this film, Oda also provided the character design for and executive produced the subsequent movies Z (2012), Gold (2016), Stampede (2019), and Red (2022).

Oda and Akira Toriyama created a 2007 crossover one-shot called Cross Epoch, that contains characters from Toriyama's Dragon Ball and Oda's One Piece. In 2013, they each designed a Gaist character for the video game Gaist Crusher.[23] In 2011, Oda and Mitsutoshi Shimabukuro created the One Piece and Toriko crossover one-shot Taste of the Devil Fruit. Shimabukuro stated that he came up with the bulk of the story while Oda gave suggestions
"""

    summary_template = """
    given the information {information} about the person I want you to create:
    1. A short summary
    2. two interesting fact about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # llm = ChatOllama(model="gpt-oss:latest")

    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})


    print(response.content)


if __name__ == "__main__":
    main()
