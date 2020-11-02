import scala.io.Source

object Task1 {
	// takes in a string text and outputs a mutable map[string int]
	def wordCount(text : String): scala.collection.mutable.Map[String, Int] = {
		// create map
		var wordCountMap = scala.collection.mutable.Map[String, Int]()
		// test data
		wordCountMap("hello") = 1
		// turn all into lowercase
		val text_lowercase = text.toLowerCase()
		// turn string into words not characters
		val words = text_lowercase.split(" ")


		for (i <- words){
			if (wordCountMap.contains(i)){
				wordCountMap(i) += 1

			}
			else{
				wordCountMap(i) = 1 
			}

		}
		return wordCountMap
	}

	def main(args: Array[String]){

	val source = Source.fromFile("Shakespeare.txt")
	val lines = source.getLines
	var text = " "
	var num = 1
	while(lines.hasNext){
		text = text + lines.next
		num += 1
		println(num + " out of 124457")

	}
	source.close
	text = text.replaceAll("[-+.^:,*]"," ");
	println(wordCount(text))

	






		
	}
}