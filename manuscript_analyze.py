### This module relys on the verb, noun, adjective, and adverb
### lists to be well organized and comprehensive
### As an app it will give robust feedback on a piece of writing

### As far as process think of this as a teacher correcting a paper.

class SentenceObject(object):
	
	"""
	This is an object that assembles the information we garner from the 
	sentence.  Gonna be a lot of those.
	"""

	def __del__(self):
		del self
	
	def __new__(self):
		pass
		
	def __init__(
		self, 
		sentence = "This is a sentence",
		number = 1, 
		case = "Declarative", 
		tense = "Present",
		):
		
		self.number = number
		self.sentence = sentence
		self.case = case
		self.tense = tense
		
	def construct(self):
		
		'''
		Construct a dictionary with the info about a sentence.
		'''
		
		sentenceInfo = {
		"name/number" : self.number,
		"case" : self.case,
		"tense" : self.tense,
		}
		
		return sentenceInfo

	def close(self):
		self.__del__()



class ManuscriptAnalyzer(object):
	
	"""
	This object holds the functions that parse and returns
	a very large dictionary of info on a 
	manuscript.   
	"""

	from nounlist import nounList
	from verblist import verbList
	from adjectivelist import adjectiveList
	from adverblist import adverbList

	
	
	def __init__(self):
		self.nounlist = nounList
		self.verblist = verbList
		self.adjectivelist = adjectiveList
		self.adverblist = adverbList
		
		self.article_list = ['the','a']
		self.conjunction_list = ['and','or', 'because', 'so']
		self.function_list = ['if', 'that', 'which']
		self.question_func = ['who', 'what', 'where', 'why', 'how']

		
		
	def close(self):
		
		del self


		
	def sentenceSplitter(manu):
		
		#Iteration 0.1
		'''
		
		'''
				
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


		
	def wordcounter(self, manu):
		
		##ITeration 0.1
		'''returns word counts for the manuscript
		as 
		(wordcount, nouns, verbs, adjectives, adverbs, unknown)
	
		'''
		nouns = 0
		verbs = 0
		adjectives = 0 
		adverbs = 0
		unknown = 0
		wordcount = 0
		
		for word in manu.split():
			
			word = word.lower()
			
			wordcount += 1
			
			if word in self.nounlist:
				nouns += 1
				
			elif word in self.verblist:
				verbs += 1
				
			elif word in self.adjectivelist:
				adjectivelist += 1
				
			elif word in self.adverblist:
				adverbs += 1 

			else:
				unknown += 1
				
		info_tuple = (
		wordcount, nouns, verbs, adjectives, adverbs, unknown
		)
		
		return info_tuple
		
		
		
	def __sentenceParser(self, manu):
	
		'''
		This function will generate a string of numbers that can be 
		read to determine the grammar of a sentence.
		
		It tests for and accepts only one sentence at a time.
		'''
	
		
		### These are 'constants' that are used to generate number
		### codes that can be used to determine a grammatical case.
		
		
		ARTICLES = '1'
		SUBJECT = '2'
		VERB = '3'
		OBJ = '4'
		PREP = '5'
		CONJUNCTIONS = '6'
		FUNCTION = '7'
		
		op_code = ''
	
	
		
		########RETHINK AND REWRITE THIS SECTION
		
		"""
		This function parses and analyzes sentences for:
		
		Tense,
		Case, 
		Type,
		Composition,
		
		"""
	
		
	
	def grammar_parse(op_nums):
		'''Reads the numbers of an opcode and gives us a 
		breakdown of:
		
		case (interrogative, imperative, declarative, descriptive)
		voice (passive, active),
		grammar fundamentals,
		
		///iteration 2.0 - can find mistakes. 
		'''
	

	def report(self, manu):
		
		"""
		Use this one.  
		This assembles all of the information into 
		a dictionary and returns it
		
		"""
		
		pass
		
		
	
###################TESTING AREA############################

#anal = ManuscriptAnalyzer()

#print anal.wordparser("The man is quickly eat cat")


##################FINAL SPACE ######################


if __name__ == "__main__":
	pass
