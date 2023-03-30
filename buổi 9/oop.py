class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
    def main():
        f = Flight(origin="New Work", destination="Paris", duration=540)
        f.duration += 10
        
        print(f.origin)
        print(f.destination)
        print(f.duration)
    if __name__ == "_main_":
        main()
        
class Flight:
    def __init__(self,origin,destination,duration):
        self .origin = origin
        self .destination = destination
        self .duration = duration
    def print_info(self):
        print(f"Flight origin:{self.origin}")
        print(f"Flight destination:{self.destination}")
        print(f"Flight duration:{self.duration}")
            
def main():
    f1 = Flight(origin="New York",destination="Paris",duration=540)
    f1.print_info()
    f2 = Flight(origin="Tokyo",destination="Shanghai",duration=185)
    f2.print_info()
if __name__ == "__main__":
    main()