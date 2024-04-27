import math

points = [(2, 3), (5, 7), (-2, 1), (8, 9), (0, 0)]  #Noktaları tanımladık

def euclideanDistance(point1, point2):
    x1, y1 = point1                                   #öklid mesafesini bulmak için fonksiyon tanımladık
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

distances = []
for i in range(len(points)):                         #Mesafelerin hesaplanması için 
    for j in range(i+1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)                #Minimum mesafesinin hesaplanması