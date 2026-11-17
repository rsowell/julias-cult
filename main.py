import asyncio
from pathlib import Path

import pygame

WIDTH, HEIGHT = 900, 650
ASSETS = Path(__file__).parent / "assets"
VISIBLE_LINES = 19


def story(say, play):
    play('Patch 1.ogg')
    say('Your name is Jake Stephens, You gaze upon your dark room, curious of what might have awakened you on such a silent night. The moonlight shines through your curtained window, illuminating your dark oak floors and cedar bedframe. Its perfect rays indicate that the moon is high in the sky, because in any other position, the pines form a thick forest that blocks the light. Suddenly, you hear the culprit: the sound of an engine exploding. You’ve heard this sound before, so you know it well')
    (yield 'Press Enter to Continue...')
    say('Plagued with concern, you jump out of bed, slip on your boots, and venture light-free onto the dark trail. Your eyes begin to adjust, which is not difficult due to the moonlight. The smell of fresh leaves begins to fill the air as you crunch them under your large, chunky boots')
    say('Outside, you notice a car wreck nearby')
    (yield 'Type Enter to continue...')
    say('Head towards the wreck')
    say('As you approach, you see something strange')
    say('You stumble upon a driver, who appears unconscious. He looks like he could be in his twenties, and wears the regular Sewanee attire for someone of that age: khaki pants and a striped polo. His body is intact–nothing appears broken. You reach out to check his pulse, but you are not a trained doctor')
    say('Inspect the mans invetory')
    say('1. Search the man')
    say('2. unfold the mysterious paper')
    choice1 = (yield 'Enter your choice (1 or 2): ')
    if choice1 == '1':
        say('You carefully search the unconscious man.')
    say('You find: gum, toothpicks, a lighter, a switchblade, and a mysterious piece of paper')
    say('Take everything')
    choice2 = (yield 'Type 2 to read the paper, or press Enter to continue.')
    if choice2 == '2':
        say('You unfold the mysterious piece of paper. It reads')
    say('"A new age is coming for us soon. A mortal will embrace our kind and then we will conquer the living world."')
    say('You are standing frozen not knowing what to do')
    (yield 'Press Enter to go back to your cabin')
    say('You are back in the cabin. You are still in shock and are debating what to do. You decide to pour yourself a cup of coffee. as the lean over to grab a cup you notice the paper falls, you pick up the paper and look at the paper again and you notice that the back of the paper says All Saints Chapel. You notice this but notice it is late.')
    (yield 'press enter to continue')
    say('you decide to go to bed forget about all this crazy stuff, you then go to sleep when suddenly in the middle of the night you start having a nightmare and you are outside all saints then suddenly it blows up in fumes, then you wake up and you hear noises from outside, you decide that there must be something going on in all saints, you decide it is time to go there')
    command = (yield 'Type `go explore all saints` and press Enter.').lower().strip()
    play('Traces.ogg')
    if command == 'go explore all saints':
        say('You push open the heavy wooden doors and step inside All Saints Chapel.')
    say("You look around and see the wooden pews that lead to the altar and you see the glass windows. You are trying to find this so called cult. But can't find anything so you keep searching. You read trough all the things on the walls when suddenly you hear a noise.")
    command = (yield 'Type `explore the noise` and press Enter.').lower().strip()
    if command == 'explore the noise':
        say('you carefully follow the noise, which leads you past the pews and past the alter, you go deeper in the chapel then you see a door that leads to a basement. It is dark so you use the lighter from earlier, you flick it on and you can see just a little  better. the sounds turn into wishpers and you make a few steps down before you hear, come we are friendly. You bolt out of the room and run out of the chapel and run all the way back to the cabin.')
    yield 'Press Enter to continue...'
    say('you get back to the cabin and notice a book on your shelf called the history of All Saints.')
    command = (yield 'Type `read the book` and press Enter.').lower().strip()
    if command == 'read the book':
        say('you start reading the book and it says, for many years there were wishpers and rumors of a cult at the bottom of all saints. But these rumors were never confirmend, however there were many who said they were going to explore the chapel. But they went missing after a few weeks. Only one who came back afterwards is an elderly man, Mac Dean. But ever since his explore he has been almost entirely mute, as a matter of fact he still lives in Sewanee to this day. You notice that his house isnt far.')
    (yield 'Press Enter to go to his house...')
    say('you go to Macs house and knock on the door. You are greated by his wife, she says what do you want honey? You say I want to talk to Mac about all saints. She says we havent been able to speak for years come on in. You see mac in his chair looking at a TV. You Sit down and his wife leaves the room. You ask him is it true what all they say about all saints? He looks at you and then looks away. You then say I am exploring it and I have read their note about a mortal who will embrace them, Mac then looks at you and grabs you by the shirt, then says in a slow voice, whatever you do dont except the power. Then he dies on the spot, being scared and not knowing what to do you leave.')
    say('you decide to go back home and think it all through. There has to be something really going on down in that basement. I must go down there and figure out what this power is.')
    (yield 'Press Enter to go back to all saints')
    say('as you head towards your door you see all the sudden the Sherif outside your cabin, sherif says come out you are wanted for the murder of Mac Dean. Not knowing what to do you open up the back window and decide to run into the woods. You think about aproaching the Sheriff but you know you need to go All Saints.')
    (yield 'Press Enter to go back to all saints to continue...')
    say('you go to all saints your facing the wooden doors, you start to wonder if this a good idea')
    command = (yield 'Type `open the door` and press Enter.').lower().strip()
    if command == 'open the door':
        say('you try to open the doors then BANG, something hits you on the top of the head and you fall unconscious')
    (yield 'Press Enter to Continue...')
    say('You wake up, your back against a dirt wall. The light hurts your eyes still, and they are slow to open. Then, you realize that the light is flames, seven of them, and they are floating. Wait, no. They are torches being held, you see what seems to be a female in robes, you ask who are?')
    (yield 'Press Enter to Continue...')
    say('the voice says so what will it be?')
    (yield 'Press Enter to Continue...')
    say("you ask what do you mean? she says it's tradition you found us, so you must become one of us, you then ask do I have a choice, she looks at you for a split second then raises her hands, a ritual is starting you try to escape")
    command = (yield 'Type `escape` and press Enter.').lower().strip()
    play('Decision.ogg')
    if command == 'escape':
        say("it's too late the ritual has already started, The robed men begin to form a circle. The woman then opens the book, and startles you with her loud, high pitched voice as she screams a latin verse. She raises the book, and the men recite her gibberish in their low tone, at a much slower pace than she. You stare at the bottom of the book. The markings on the front are the same that you saw earlier at the top of the cave. The ritual goes on for minutes, the men circling around the woman.")
        (yield 'Press Enter to Continue...')
        say('the ritual ends and you feel this power but you realize you must reject the power Mac warned you about')
        command = (yield 'Type `reject the power` and press Enter.').lower().strip()
        if command == 'reject the power':
            say('as you start rejecting the power you remember that you have the lighter in your pocket and a flask with rum, you put a little bit in your mouth and get ready to ingite the lighter, the lady then ask so what will it be? You spit the rum on her and she looks at you enraged then you say, burn')
            say('you flip your lighter and start to ignite it')
            command = (yield 'Type `ignite lighter` and press Enter.').lower().strip()
            if command == 'ignite lighter':
                say('she starts burning and all the men behind her start panicing, she takes her robe off shes wearing all black, she uses telekinesis to pull you toward her, she says I thought you would be the one you showed so much promise too bad it has to end this way, you remeber you have the switchblade in your pocket, you say world to manipulate her she then says, become one with us, join me, kiss me boy, she has let her guard down now you have a chance to end it')
                command = (yield 'Type `kill her` and press Enter.').lower().strip()
                if command == 'kill her':
                    say('it works you stab her and now shes bleeding as she starts bleeding, as shes dying a blue shadow of spirits start coming out of her and everyone else in the room, it goes on for a few seconds then all the sudden they all turn to ash, you look around and you see all the ashes you feel like you have saved the sewanee community, then all the sudden the building starts shaking you sit there and you start to think the police departmen is already after you for murder and youve already saved the community why dont you just sit and have it all end here')
                    (yield 'press Enter to continue')
                    say('then suddenly you feel someone grab your shoulder and it is the sherif, he says lets go, you both run out of all saints and you barely make it, you both take a second to breathe, the sherif then says that was crazy, you then say yeah it was, well take me in chief, you put out your hands but the sherif pushes them down then says, you have saved this community that dosent deserve an arrest, go home')
    (yield 'press Enter to continue')
    say("then suddenly you hear something and it is one of the men that was downstairs all bloody and he says this is not over you will pay for what you have done there is no escaping your fate you are cursed you think you saved this community? You have only put it in more danger, then suddenly the sherif shoots him in the face. Sherif looks at you and says go home I'll take it from here.")
    (yield 'press Enter to continue')
    say('you head back home and feel confused, after all you have seen in that basement you dont know how to rest of your life will go or even if it will be normal, you say a prayer and then go to bed')
    (yield 'press Enter to continue')
    say('Jake Stephens went on to meet his wife at church and had 4 kids with her, after this he became a police officer, using the new advantages he had as a officer he went on hunt supernatural incidents, saved many lives and would go on to pass at the ripe age of 96 a year after his wife died')
    say('game over')


def wrap(text, font, width):
    line = ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if line and font.size(candidate)[0] > width:
            yield line
            line = word
        else:
            line = candidate
    yield line



async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jake Stephens")
    title_font = pygame.font.Font(None, 44)
    font = pygame.font.Font(None, 26)
    clock = pygame.time.Clock()

    sounds = {}
    if pygame.mixer.get_init():
        for name in ("Patch 1.ogg", "Traces.ogg", "Decision.ogg"):
            path = ASSETS / name
            if path.is_file():
                try:
                    sounds[name] = pygame.mixer.Sound(str(path))
                except pygame.error as error:
                    print(f"Could not load {name}: {error}")

    def play(name):
        if name in sounds:
            sounds[name].play()

    lines = []

    def say(message):
        lines.extend(wrap(message, font, WIDTH - 64))

    game = story(say, play)
    prompt = next(game)
    first_line = 0
    command = ""
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                first_line = max(0, min(len(lines) - VISIBLE_LINES, first_line - 3 * event.y))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_PAGEUP:
                    first_line = max(0, first_line - VISIBLE_LINES + 1)
                elif event.key == pygame.K_PAGEDOWN:
                    first_line = max(0, min(len(lines) - VISIBLE_LINES, first_line + VISIBLE_LINES - 1))
                elif prompt is None:
                    if event.key == pygame.K_r:
                        for sound in sounds.values():
                            sound.stop()
                        lines.clear()
                        game = story(say, play)
                        prompt = next(game)
                        first_line = 0
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    answer = command
                    command = ""
                    if answer:
                        say(f"> {answer}")
                    say("")
                    try:
                        prompt = game.send(answer)
                    except StopIteration:
                        prompt = None
                    first_line = max(0, len(lines) - VISIBLE_LINES)
                elif event.key == pygame.K_BACKSPACE:
                    command = command[:-1]
                elif event.unicode and event.unicode.isprintable():
                    command = (command + event.unicode)[:60]

        screen.fill((28, 24, 37))
        screen.blit(title_font.render("Jake Stephens", True, (236, 201, 118)), (32, 24))
        for row, line in enumerate(lines[first_line:first_line + VISIBLE_LINES]):
            screen.blit(font.render(line, True, (244, 239, 247)), (32, 80 + row * 24))
        pygame.draw.line(screen, (121, 107, 137), (32, 553), (WIDTH - 32, 553))
        hint = prompt if prompt is not None else "Press R to restart."
        screen.blit(font.render(hint.replace("`", ""), True, (236, 201, 118)), (32, 568))
        if prompt is not None:
            screen.blit(font.render("> " + command + "_", True, (244, 239, 247)), (32, 598))
        pygame.display.flip()
        clock.tick(30)
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
