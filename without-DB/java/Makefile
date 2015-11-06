.PHONY : clean

main := CompareRecommenders
classes := classes
sources := sources

$(classes)/$(main).class : $(sources)/*.java
	mkdir -p output
	mkdir -p $(classes)
	javac -sourcepath $(sources) -d $(classes) $(sources)/$(main).java
	java -classpath $(classes) $(main)

clean :
	rm -r output
	rm -r $(classes)
