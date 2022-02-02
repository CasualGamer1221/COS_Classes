# File:parent_Project1-XC.py
# Author: Jeffery Parent
# Date: November 18, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Creates a graph using name rank data from the SSA, and shades below the graphed line.

# Collaboration:
# I didn't discuss this assingment with anyone.

from graphics import *

##### DRAW GRAPH ####
def draw_graph(line_Data):
    

    #Window
    window_Length=1200 ; window_height=800 # 1600 points
    win = GraphWin("My Drawing", window_Length, window_height)
    #Sets LL corner to be (0,0) and TR corner to be (1200,1600)
    win.setCoords(0, 0, window_Length, window_height*2)
   
    
    
    #Loop for vertical lines and Axis Labels
    for i in range(0,11):
        #Offsets and other things
        graph_x_offset=200 ; graph_y_offset = 200 ; graph_height= 1000 + graph_y_offset ; graph_width_iterated= (graph_x_offset+(i*90)) ; graph_height_iterated = (graph_y_offset+(i*100))
        
        #Decade Lines
        aLine =Line(Point(graph_width_iterated,graph_height), Point (graph_width_iterated, graph_y_offset))
        aLine.setOutline("black")
        aLine.draw(win)
        
        #Rectangle outline
        graph_x_max = (graph_x_offset+900)  ; graph_y_max = (graph_y_offset+1000)
        
        aRectangle = Rectangle(Point(graph_x_offset , graph_y_offset), Point(graph_x_max,graph_y_max))
        aRectangle.setOutline("black")
        aRectangle.setWidth(2)
        aRectangle.draw(win)
    
        #X-Axis Labels
        start_year=1900 ; text_y_offset_years= (graph_x_offset - 50)
        x_Label = Text(Point(graph_width_iterated,text_y_offset_years), (start_year+(i*10)))
        x_Label.setFace("times roman")
        x_Label.draw(win)    

        #Y-Axis Labels
        text_y_offset_rank = (graph_y_offset - 50); start_rank=900 ; offset2 = 100
        
        #Adds labels and lines along y-axis
        while i < 9:
            
            y_Label=Text(Point(text_y_offset_rank , (graph_height_iterated+offset2)), (start_rank-(i*100)))
            y_Label.setFace("times roman")
            y_Label.draw(win)
            
            y_label_line_offset_a=graph_y_offset*0.95
            y_label_line_offset_b=graph_y_offset*1.05
            
            y_Label_line = Line(Point(y_label_line_offset_a , graph_height_iterated+offset2), Point(y_label_line_offset_b, graph_height_iterated+offset2))
            y_Label_line.setOutline("black")
            y_Label_line.draw(win)
            break
        y_label_highest=Text(Point(text_y_offset_rank,graph_height) , (1))
        y_label_lowest=Text(Point(text_y_offset_rank,graph_y_offset) , (0))
        
        y_label_highest.setFace("times roman")
        y_label_lowest.setFace("times roman")
        y_label_highest.draw(win)
        y_label_lowest.draw(win)
        
        # Graph lines   
        while i < 10:
            lowest_rank=1000
            
            graph_width_iterated_2= ((graph_x_offset+90)+(i*90))
            
            if (int(line_Data[1+i])) != 0:
                position1=Point(graph_width_iterated , (abs(lowest_rank-(int(line_Data[1+i]))) + graph_y_offset))
                position1_label = Point(graph_width_iterated , (abs(lowest_rank-(int(line_Data[1+i]))) + graph_y_offset*1.4))
            elif (int(line_Data[1+i])) == 0:
                position1=Point(graph_width_iterated , (0 + graph_y_offset))
                position1_label=Point(graph_width_iterated , (0 + graph_y_offset*1.4))
            if (int(line_Data[2+i])) != 0:
                position2=Point(graph_width_iterated_2 , (abs(lowest_rank-(int(line_Data[2+i]))) + graph_y_offset))
                position2_label=Point(graph_width_iterated_2 , (abs(lowest_rank-(int(line_Data[2+i]))) + graph_y_offset*1.4))
            elif (int(line_Data[2+i])) == 0:
                position2=Point(graph_width_iterated_2 , (0 + graph_y_offset))
                position2_label=Point(graph_width_iterated_2 , (0 + graph_y_offset*1.4))
            
            
           
            
            line = Line(position1,position2)
            line.setOutline("blue")
            line.draw(win)
            
            shading=Polygon(position1,position2,Point(graph_width_iterated_2,graph_y_offset),Point(graph_width_iterated,graph_y_offset))
            shading.setFill(color_rgb(103, 230, 208))
            shading.draw(win)
            
            #Graph Title
            graph_title = Text(Point((window_Length//2) , (window_height*2)-100) , (f'{line_Data[0]} Name Popularity'))
            graph_title.setFace("times roman")
            graph_title.setSize(18)
            graph_title.draw(win)
            
            #Graph x-axis Title
            graph_x_title = Text(Point((window_Length//2) , graph_x_offset-100) , (f'Year'))
            graph_x_title.setFace("times roman")
            graph_x_title.setSize(14)
            graph_x_title.draw(win)
            
            #Graph Y-axis Title
            graph_x_title = Text(Point((graph_x_offset*.3) , graph_height//2) , (f'Rank (1 is highest)'))
            graph_x_title.setFace("times roman")
            graph_x_title.setSize(10)
            graph_x_title.draw(win)
            
            point_label =Text((position1_label), ("(",line_Data[0] ,",", line_Data[1+i],")"))
            point_label.setFace("times roman")
            point_label.setSize(8)
            point_label.draw(win)
            
            if i == 9:
                point_label_last = Text((position2_label), ("(",line_Data[0] , ",", line_Data[2+i],")"))
                point_label_last.setFace("times roman")
                point_label_last.setSize(8)
                point_label_last.draw(win)
            break
    

    win.getMouse() # pause for click in window
    win.close()


#### GET DATA ####
def get_data(search_value):
    f=open("names_data.txt" , "r")
    for line in f:
        if (line.split()[0]) == str(search_value):
            return line.split()
        else: continue
            

def main():
    print()
    print("This will create a graph using name ranking data obtained from the Social Security Administration from the year 1900 to 2000")
    print()
    line_Data = get_data(input("What name do you want rank data to be graphed for? ").lower().title())
    if line_Data == None:
        print("Name not found!!")
    else:
        draw_graph(line_Data)
    
    
main()


