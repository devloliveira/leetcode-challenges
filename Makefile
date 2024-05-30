SRCS=*.cpp
OBJS=$(subst .cc,.o,$(SRCS))


%.o: %.cpp
	g++ -c $<


solution: $(OBJS)
	g++ $< -o a

clean:
	rm -f *.o
	rm -f a
