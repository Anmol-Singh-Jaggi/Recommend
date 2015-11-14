.PHONY : clean
.PHONY : run

main := CompareRecommenders
classes := classes
sources := sources

run : $(classes)/$(main).class
	java -classpath $(classes) $(main)

$(classes)/$(main).class : $(sources)/*.java
	mkdir -p output
	mkdir -p $(classes)
	javac -sourcepath $(sources) -d $(classes) $(sources)/$(main).java

clean :
	rm -r output
	rm -r $(classes)
