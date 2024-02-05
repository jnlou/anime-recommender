
import anime_recommending
# very long test case of animes with their matching genres
genres = {'Comedy' : ['Saiki K', 'One Punch Man', 'Gintama', 'Shimoneta', 'Assassination Classroom', "Haven't You Heard? I'm Sakamoto", 'Ghost Stories', "Monthly Girls' Nozaki-kun",
                     'Daily Lives Of High School Boys', 'Ouran High School Host Club', 'The Devil Is A Part-Timer!', 'Great Teacher Onizuka', 'FLCL', 'Kaguya-sama: Love Is War'],
          'Action' : ['Kill La Kill', 'Attack on Titan', 'Bleach', "JoJo's Bizarre Adventures", 'Cowbow Bebop', 'Jujutsu Kaisen', 'Naruto', 'Sword Art Online', 'Dragon Ball Z', 
                      'Fullmetal Alchemist', 'Seraph of the End', 'Baki', 'Hellsing', 'King of Thorn', 'Castlevania', 'Black Butler', 'Demon Slayer', 'Tokyo Ghoul', 
                      'My Hero Academia', 'Chainsaw Man', 'Fire Force'],
          'Adventure' : ['The Promised Neverland', 'Mushoku Tensei: Jobless Reincarnation', 'Hunter x Hunter', 'Vinland Saga', 'Goblin Slayer', 'Seven Deadly Sins', 'Fairy Tail',
                        'Doctor Stone', 'One Piece', 'Overlord', 'That Time I Got Reincarnated as a Slime', 'Is It Wrong to Try to Pick Up Girls in a Dungeon?',
                        'Made in Abyss', 'Log Horizon'],
          'Romance' : ['Toradora!', 'Fruits Basket', 'InuYasha', 'Horimiya', 'Tsuki ga Kirei', "The Ancient Magus' Bride", 'High School DxD', 'My Happy Marriage', "Shikimori's Not Just a Cutie",
                       'Clannad', 'Your Lie In April', 'Nana', 'Vampire Knight', 'Welcome To The N.H.K.', 'Sing "Yesterday" For Me', 'Kimi Ni Todoke: From Me To You', 'Maid Sama!',
                       'Rascal Does Not Dream Of Bunny Girl Senpai', 'My Dress-Up Darling', 'The Pet Girl Of Sakurasou', 'School Days'],
          'Horror' : ['Parasyte: The Maxim', 'Another', 'Corpse Party: Tortured Souls', 'Deadman Wonderland', 'Devilman Crybaby', 'Elfen Lied', 'Gantz', 'Ghost Hunt', 'Junji Ito Collection',
                      'Mushi-shi', 'School-Live!', 'Serial Experiments Lain', 'Shiki', 'Yamishibai: Japanese Ghost Stories', 'Highschool of the Dead', 'Tokko', 'When They Cry: Higurashi', 'The World Yamizukan'],
          'Suspense' : ['Death Note', 'The Flowers of Evil', 'Hell Girl', 'Paranoia Agent', 'Kakegurui', 'Erased', 'Steins;Gate', 'The Future Diary', 'Death Parade', 'Terror in Resonance',
                        'Monster', 'From the New World', 'Psycho Pass', 'Moriarty the Patriot', 'Platinum End', 'ID: Invaded', 'Tomodachi Game',
                        'My Home Hero', 'Ceres, Celestial Legend']
          }
# very long test case of animes with their matching streaming platforms
platforms = {'Netflix' : ['Saiki K','One Punch Man', "Monthly Girls' Nozaki-kun", 'Ouran High School Host Club', 'Bleach', "JoJo's Bizarre Adventures", 'Cowbow Bebop', 'Naruto',
                          'Sword Art Online', 'Dragon Ball Z', 'Fullmetal Alchemist', 'Baki', 'Castlevania', 'Black Butler', 'Demon Slayer', 'The Promised Neverland',
                          'Mushoku Tensei: Jobless Reincarnation', 'Hunter x Hunter', 'Vinland Saga', 'Seven Deadly Sins',  'One Piece', 'Is It Wrong to Try to Pick Up Girls in a Dungeon?',
                          'Toradora!', 'InuYasha', 'My Happy Marriage', 'Kimi Ni Todoke: From Me To You', 'Rascal Does Not Dream Of Bunny Girl Senpai',  'My Dress-Up Darling',
                          'Parasyte: The Maxim', 'Devilman Crybaby', 'The Flowers of Evil', 'Kakegurui', 'Erased', 'Monster'],
             'Hulu' : ['One Punch Man','Gintama','Assassination Classroom', 'Ouran High School Host Club', 'The Devil Is A Part-Timer!', 'FLCL', 'Kaguya-sama: Love Is War',
                       'Kill La Kill', 'Attack on Titan', 'Bleach', "JoJo's Bizarre Adventures", 'Cowbow Bebop', 'Naruto', 'Sword Art Online', 'Dragon Ball Z', 'Fullmetal Alchemist',
                       'Seraph of the End', 'Hellsing', 'Black Butler', 'Demon Slayer', 'Tokyo Ghoul', 'My Hero Academia', 'Chainsaw Man', 'Fire Force', 'The Promised Neverland',
                       'Mushoku Tensei: Jobless Reincarnation', 'Hunter x Hunter', 'Fairy Tail', 'Doctor Stone',  'One Piece', 'Overlord', 'That Time I Got Reincarnated as a Slime',
                       'Is It Wrong to Try to Pick Up Girls in a Dungeon?', 'Made in Abyss', 'Log Horizon', 'Fruits Basket', 'InuYasha', 'Horimiya', 'High School DxD', 'Your Lie In April',
                       'Nana', 'Vampire Knight', 'Kimi Ni Todoke: From Me To You', 'Maid Sama!', 'Rascal Does Not Dream Of Bunny Girl Senpai', 'Parasyte: The Maxim', 'Mushi-shi',
                       'When They Cry: Higurashi', 'Death Note', 'Erased', 'Steins;Gate', 'The Future Diary', 'Death Parade', 'Psycho Pass', 'Platinum End', 'ID: Invaded'],
             'Crunchyroll' : ['Saiki K','One Punch Man','Gintama', 'Shimoneta','Assassination Classroom',"Haven't You Heard? I'm Sakamoto", 'Ghost Stories', "Monthly Girls' Nozaki-kun",
                              'Daily Lives Of High School Boys', 'Ouran High School Host Club', 'The Devil Is A Part-Timer!', 'Great Teacher Onizuka', 'FLCL', 'Kaguya-sama: Love Is War',
                              'Kill La Kill', 'Attack on Titan', 'Bleach', "JoJo's Bizarre Adventures", 'Cowbow Bebop', 'Jujutsu Kaisen', 'Naruto', 'Sword Art Online', 'Dragon Ball Z',
                              'Fullmetal Alchemist', 'Seraph of the End', 'Baki', 'Hellsing', 'King of Thorn', 'Black Butler', 'Demon Slayer', 'Tokyo Ghoul', 'My Hero Academia',
                              'Chainsaw Man', 'Fire Force', 'The Promised Neverland', 'Mushoku Tensei: Jobless Reincarnation', 'Hunter x Hunter', 'Vinland Saga', 'Goblin Slayer',
                              'Fairy Tail', 'Doctor Stone',  'One Piece', 'Overlord', 'That Time I Got Reincarnated as a Slime', 'Is It Wrong to Try to Pick Up Girls in a Dungeon?',
                              'Made in Abyss', 'Log Horizon', 'Fruits Basket', 'InuYasha', 'Horimiya', 'Tsuki ga Kirei', "The Ancient Magus' Bride", 'High School DxD',
                              'My Happy Marriage',  "Shikimori's Not Just a Cutie", 'Your Lie In April', 'Nana', 'Vampire Knight', 'Welcome To The N.H.K.', 'Sing "Yesterday" For Me',
                              'Kimi Ni Todoke: From Me To You', 'Maid Sama!', 'Rascal Does Not Dream Of Bunny Girl Senpai',  'My Dress-Up Darling', 'The Pet Girl Of Sakurasou',
                              'School Days', 'Parasyte: The Maxim', 'Another', 'Corpse Party: Tortured Souls', 'Deadman Wonderland', 'Elfen Lied', 'Gantz', 'Ghost Hunt', 'Junji Ito Collection',
                              'Mushi-shi', 'School-Live!', 'Serial Experiments Lain', 'Shiki', 'Yamishibai: Japanese Ghost Stories', 'Tokko', 'When They Cry: Higurashi', 'The World Yamizukan',
                              'Death Note', 'The Flowers of Evil', 'Hell Girl', 'Paranoia Agent', 'Erased', 'Steins;Gate', 'The Future Diary', 'Death Parade', 'Terror in Resonance',
                              'From the New World', 'Psycho Pass', 'Moriarty the Patriot', 'Platinum End', 'ID: Invaded', 'Tomodachi Game', 'My Home Hero', 'Ceres, Celestial Legend'],
             'Funimation' : ['Saiki K', 'Shimoneta','Assassination Classroom', 'Daily Lives Of High School Boys', 'Ouran High School Host Club' 'The Devil Is A Part-Timer!', 'FLCL',
                             'Kaguya-sama: Love Is War', 'Kill La Kill', 'Attack on Titan', 'Cowbow Bebop', 'Jujutsu Kaisen', 'Naruto', 'Sword Art Online', 'Dragon Ball Z', 'Fullmetal Alchemist',
                             'Seraph of the End', 'Hellsing', 'King of Thorn', 'Black Butler', 'Demon Slayer', 'Tokyo Ghoul', 'My Hero Academia', 'Fire Force', 'The Promised Neverland',
                             'Mushoku Tensei: Jobless Reincarnation', 'Goblin Slayer', 'Seven Deadly Sins', 'Fairy Tail', 'Doctor Stone', 'One Piece', 'Overlord', 'That Time I Got Reincarnated as a Slime',
                             'Log Horizon', 'Toradora!', 'Fruits Basket', 'Horimiya', 'Tsuki ga Kirei', "The Ancient Magus' Bride", 'High School DxD', 'Clannad', 'Your Lie In April',
                             'Welcome To The N.H.K.', 'Kimi Ni Todoke: From Me To You', 'Rascal Does Not Dream Of Bunny Girl Senpai',  'My Dress-Up Darling', 'Deadman Wonderland', 'Gantz',
                             'Ghost Hunt', 'Junji Ito Collection', 'Mushi-shi', 'Serial Experiments Lain', 'Shiki', 'When They Cry: Higurashi', 'Paranoia Agent', 'Erased', 'Steins;Gate', 'The Future Diary',
                             'Death Parade', 'Terror in Resonance', 'Psycho Pass', 'Moriarty the Patriot', 'Platinum End', 'ID: Invaded']
            }
def main(): 
    user = anime_recommending.get_user_genre(genres)
    number = anime_recommending.get_anime_amount(genres)
    anime_recommending.rec_user_anime(user, number, platforms, genres)

main()


