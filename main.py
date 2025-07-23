import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.LIGHTBLUE_EX} ✨Welcome to Sentiment analyser🔍🔎✨{Style.RESET_ALL}")
user_name = input(f"{Fore.LIGHTGREEN_EX}Please enter your name:{Style.RESET_ALL}").strip()
if not user_name:
    user_name ="Sherlock Holmes" 
conversation_history=[]
print(f'{Fore.LIGHTCYAN_EX}Hello, Agent {user_name}!')
print(f"Type a sentence and the analiser will analyse🤖 it for you")
print(f"{Fore.GREEN}Type reset,{Fore.LIGHTYELLOW_EX}Type history🕰️,{Fore.RED}Exit to quit😏😏😏{Style.RESET_ALL}\n")
while True:
    user_input=input(f"{Fore.LIGHTRED_EX}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}🚨🚨🚨Please enter a sentence to analyze{Style.RESET_ALL}")
        continue
    elif user_input.lower()== "exit" or "quit":
        print(f"\n{Fore.LIGHTMAGENTA_EX}Exiting Program....🙋‍♂️Bye Agent{user_name}👋👋👋{Style.RESET_ALL}")
        break
    elif user_input=="history":
        if not conversation_history:
            print(f"{Fore.RED}📜📜📜No history found{Style.RESET_ALL}")
        else :
            print(f"{Fore.YELLOW}Conversation History: {Style.RESET_ALL}")
            for idx,(text,polarity,sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                    emoji="😁"
                elif sentiment_type=="Negative":
                    color=Fore.Red
                    emoji="🥺"
                else :
                    color=Fore.YELLOW
                    emoji="😐"
                print(f"{idx}.{color}{emoji}{text}" f"(polarity{polarity:.2f},{sentiment_type}){Style.RESET_ALL}")
        continue
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity>0.25:
        sentiment_type="Positive"
        color=Fore.GREEN
        emoji="😁"

    elif polarity<-0.25:
        sentiment_type="Negative"
        color=Fore.Red
        emoji="🥺"

    else :
        sentiment_type="Neutral"
        color=Fore.YELLOW
        emoji="😐"
    conversation_history.append((user_input,polarity,sentiment_type))
    print(f"{color}{emoji}{sentiment_type}sentiment detected!" f"(polarity:{polarity:.2f}){Style.RESET_ALL}")