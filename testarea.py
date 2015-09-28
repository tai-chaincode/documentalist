test_sentence = """
Welcome to Game Proposals!

This is an early iteration of the site. Certain pieces of functionality have not been incorporated into the framework of the site so you may run into some construction signs but we promise that the core forum is up and running quite well.

We are planning on seeing how this community develops and if we manage to make something cool here work, we are prepared to expand our servers and spend more time making a place for your imagination to doodle. Likewise, the GP team is working on some community events to make sure the sites beta rolls into a full launch with as much fanfare as possible. This means we will be announcing new features, more fixes, and some awesome community events for all of you.

If you have any suggestions for these community events go ahead and send an email over to gpwebmaster406@gmail.com or send us a tweet at @gameproposals.

Likewise, we pride ourselves on being a community driven site so any suggestions/submissions for the header banner or design of the site are more than welcome... they are encouraged for we are unimaginative schmucks when placed next to the full force of the gaming community's imagination."""

def sentence_splitter(manu):
	
	masterlist = []
	workinglist = []
	punctuation = ["!","?","."]
	
	
	for letter in manu:
		
		workinglist.append(letter)
		
		if letter in punctuation:
			workingstr = ''.join(workinglist).strip()
			workingstr.replace("\n", " ")
			masterlist.append(workingstr)
			workinglist = []
			
	masterlist = [x for x in masterlist if len(x) > 1]

		
	return masterlist


print "\n".join(sentence_splitter(test_sentence))
	
