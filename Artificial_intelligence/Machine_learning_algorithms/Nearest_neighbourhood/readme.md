# The nerest neighbourhood algorithm

## Dataset:

Classes:     0=Appendizitis negativ
             1=Appendizitis positiv



Attributes:

Alter:                                       
-continuous.

Geschlecht_(1=m___2=w):	      				          
-1,2.

Schmerz_Quadrant1_(0=nein__1=ja):			          
-0,1.

Schmerz_Quadrant2_(0=nein__1=ja):			          
-0,1.

Schmerz_Quadrant3_(0=nein__1=ja):			          
-0,1.

Schmerz_Quadrant4_(0=nein__1=ja):			          
-0,1.

Lokale_Abwehrspannung_(0=nein__1=ja):			      
-0,1.

Generalisierte_Abwehrspannung_(0=nein__1=ja):		
-0,1.

Schmerz_bei_Loslassmanoever_(0=nein__1=ja):		  
-0,1.

Erschuetterung_(0=nein__1=ja):				          
-0,1.

Schmerz_bei_rektaler_Untersuchung_(0=nein__1=ja):	
-0,1.

Temp_ax:						                          
-continuous.

Temp_re:						                          
-continuous.

Leukozyten:						                        
-continuous.

Diabetes_mellitus_(0=nein__1=ja):			            
-0,1


## K-Nearest_neighbour.py

- This is an implementation of a simple KNN trained on 'app1.data' and evaluated on 'app1.test'


## Nearest_neighbor_leave_one-out_cross_validation.py

- Here the cross validation is performed and the best value for the hyper parameter 'K' in KNN algorithm is found. 
