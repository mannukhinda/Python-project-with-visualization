i=0
while(i==1) or (i<=6):
  print('.........................WELCOME TO UN-EMPLOYMENT RATE IN INDIA.........................')
  print('________________________________________________________________________________________')
  print('1.Complete Unemployed data of india using(Matplot).')
  print('2.Details according to particular State.')
  print('3.Details of Unemployment Rate and Labour Participation Rate using State.')
  print('4.Estimated Estimated Employed with State.')
  print('5.Unemployment Rate (%) & Labour Participation Rate (%) using (Monthly) Date Wise.')
  print('6.Get details according to the State for find Max and Min.')
  print('________________________________________________________________________________________')
  print('\n...................................Choose Your Option......................................\n')

  try:
    i=int(input('Enter Valid number to get the Details:'))
    break
  except ValueError:
    print("\n...............You Didn't Enter a Valid Input.")
    print('________________________________________________________________________________________\n')

while True:
  if i==0 or i>6:
    print('\n(A).......................................Thank You........................................')
    print('\n(B).....................Accept Input From User Between (1) to (6)..........................\n')
    break

  elif i==1:
    fig=px.sunburst(data_frame=df,path=['Area','Region','Date',' Estimated Employed'],hover_data=[' Estimated Unemployment Rate (%)',' Estimated Labour Participation Rate (%)'],maxdepth=2,width=1000,height=800,color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.show()
    break

  elif i==2:
    print('\n.....................................Choose Your State........................................')  
    print('______________________________________________________________________________________________\n')
    print('1.Andhra Pradesh          2.Assam          3.Bihar          4.Chhattisgarh          5.Delhi')
    print('6.Goa                     7.Gujarat         8.Haryana        9.Himachal Pradesh     10.Jammu & Kashmir')
    print('11.Jharkhand              12.Karnataka     13.Kerala        14.Madhya Pradesh      15.Maharashtra')
    print('16.Meghalaya              17.Odisha        18.Puducherry    19.Punjab              20.Rajasthan')
    print('21.Sikkim                22.Tamil Nadu    23.Tripura       24.Uttar Pardesh       25.Uttarakhand')
    print('26.West Bengal           27.Telangana')
    print('______________________________________________________________________________________________________')
    print('\n........................................Enter (0) for Exit..........................................\n')

    try:

      a=input('Choose The State which you want to see the data: ')
      if ((a.isalpha()) & (len(a)>0)):
        print()
      else :
        raise TypeError
    #except ValueError:
      #print("Sorry")
    except TypeError:
       print("It Cannot be Empty (OR) cannot have Integer Numbers.")
  
    else:
      region=df[(df['Region']==a)]  
      print('\n',region.to_markdown())
      print('______________________________________________________________________________________________________')
        

      explode=[0.03,0.03]
      data=[len(df[(df['Region']==a) & (df["Area"]=="Rural")]),len(df[(df['Region']==a) & (df['Area']=="Urban")])]
      mylabels=['Rural',' Urban']
      colors=['blue','orange']

      plt.title('\nUnemployment Data Using Selected State and (Area Wise).\n')
      plt.pie(data,labels=mylabels,explode=explode,shadow=True,colors=colors,autopct="%0.4f%%")
      plt.show()
      
      
      print('\n.......................................Thank You...................................................')
      print('\n.....................................See You Soon..................................................')
      break

  elif i==3:
    print('___________________________________________________________________________________________________')
    print('.......................................Choose your State for unemployment rate.....................')
    print('1.Andhra Pradesh          2.Assam          3.Bihar          4.Chhattisgarh          5.Delhi')
    print('6.Goa                     7.Gujarat         8.Haryana        9.Himachal Pradesh     10.Jammu & Kashmir')
    print('11.Jharkhand              12.Karnataka     13.Kerala        14.Madhya Pradesh      15.Maharashtra')
    print('16.Meghalaya              17.Odisha        18.Puducherry    19.Punjab              20.Rajasthan')
    print('21.Sikkim                22.Tamil Nadu    23.Tripura       24.Uttar Pardesh       25.Uttarakhand')
    print('26.West Bengal           27.Telangana')
    print('______________________________________________________________________________________________________')
    print('\n........................................Enter (0) for Exit..........................................\n')

    try:
      b=input('Enter The State Name Which You Want To Get The Details: ')
      if ((b.isalpha()) & (len(b)>0)):
        print()
      else :
        raise TypeError
    #except ValueError:
      #print("Sorry")
    except TypeError:
       print("It Cannot be Empty (OR) cannot have Integer Numbers.")
  
    #     print()
    #   break
    # except ValueError:
    #   print('Choose the Accurate State Name & (It Must be Case Senstive).')
    else:
      try:
        print('_____________________________________________________________________________________________________')
        print('..........................Choose the Date For results of Estimated Employees.........................')
        print('(1).31-05-2019             (2).30-06-2019            (3).31-07-2019            (4).31-08-2019')
        print('(5).30-09-2019             (6).31-10-2019            (7).30-11-2019            (8).31-12-2019')
        print('(9).31-01-2020             (10).29-02-2020           (11).31-03-2020           (12).30-04-2020')
        print('(13).31-05-2020            (14).30-06-2020')
        print('\n__________________________________________________________________________________________________')
      
        
        d = pd.to_datetime(input('Input date in (Date-Month-Year) format: '))
        df.query('Date == @d')
        
      except ValueError:
        print()
      else:        
        
        date=df[(df['Region']==b) & (df['Date']==d)]
        print(date.to_markdown())


        date[[' Estimated Unemployment Rate (%)', ' Estimated Labour Participation Rate (%)']].plot.bar()
        plt.show()
        break
        
      
      print('\n.......................................Thank You...................................................')
      print('\n.....................................See You Soon..................................................')


  elif i==4:
    print('______________________________________________________________________________________________________')
    print('.....................Choose The Area For Estimated Labour Participation Rate..........................\n')
    print('1.Andhra Pradesh          2.Assam          3.Bihar          4.Chhattisgarh          5.Delhi')
    print('6.Goa                     7.Gujarat         8.Haryana        9.Himachal Pradesh     10.Jammu & Kashmir')
    print('11.Jharkhand              12.Karnataka     13.Kerala        14.Madhya Pradesh      15.Maharashtra')
    print('16.Meghalaya              17.Odisha        18.Puducherry    19.Punjab              20.Rajasthan')
    print('21.Sikkim                22.Tamil Nadu    23.Tripura       24.Uttar Pardesh       25.Uttarakhand')
    print('26.West Bengal           27.Telangana')
    print('\n_____________________________________________________________________________________________________')
    print('\n........................................Enter (0) for Exit..........................................\n')

    try:
      c=input('Enter The State Name For (Estimated Labour Values): ')
      if ((c.isalpha()) & (len(c)>0)):
        print()
      else :
        raise TypeError
    #except ValueError:
      #print("Sorry")
    except TypeError:
       print("It Cannot be Empty (OR) cannot have Integer Numbers.")

    #   if not re.match("[azAZ]$",c):
    #     print()
    #   break
    # except ValueError:
    #   print('Choose The Accurate State Name & (It Must be Case Senstive).')
    else:
       employee=df[(df['Region']==c)]
       print(employee.to_markdown())
       
       employee[[' Estimated Employed']].plot.bar()
       plt.show()
       break




    print('.......................................Thank You...................................................')
    print('.....................................See You Soon..................................................')




  elif i==5:
    print('_____________________________________________________________________________________________________')
    print('..........................Choose the Date For results of Estimated Employees.........................')
    print('(1).31-05-2019             (2).30-06-2019            (3).31-07-2019            (4).31-08-2019')
    print('(5).30-09-2019             (6).31-10-2019            (7).30-11-2019            (8).31-12-2019')
    print('(9).31-01-2020             (10).29-02-2020           (11).31-03-2020           (12).30-04-2020')
    print('(13).31-05-2020            (14).30-06-2020')
    print('\n__________________________________________________________________________________________________')
    print('\n........................................Enter (0) for Exit..........................................\n')

    try:
      d=input('Enter The Date Which You Want To Get The Data: ')
      if ((len(d)>0)):
        print()
      else :
        raise TypeError
    #except ValueError:
      #print("Sorry")
    except TypeError:
       print("It Cannot be Empty.")

      #if not re.match("[0,9]{1,2}\\/-[0,9]{1,2}\\/-[0,9]{4}",d):
       # print()
    #   break
    # except ValueError:
    #   print('Choose the (Accurate_Pattern) Of The Date.')
    else:
      user=df[(df['Date']==d)]
      print(user.to_markdown())


      df[[' Estimated Unemployment Rate (%)',' Estimated Labour Participation Rate (%)']].plot.hist()
      plt.show()
      break


      print('.......................................Thank You...................................................')
      print('.....................................See You Soon..................................................')


  elif i==6:
    print('_____________________________________________________________________________________________________')
    print('..........................Get The Maximum & Minimum Unemployment Rate................................')
    print('1.Andhra Pradesh          2.Assam          3.Bihar          4.Chhattisgarh          5.Delhi')
    print('6.Goa                     7.Gujarat         8.Haryana        9.Himachal Pradesh     10.Jammu & Kashmir')
    print('11.Jharkhand              12.Karnataka     13.Kerala        14.Madhya Pradesh      15.Maharashtra')
    print('16.Meghalaya              17.Odisha        18.Puducherry    19.Punjab              20.Rajasthan')
    print('21.Sikkim                22.Tamil Nadu    23.Tripura       24.Uttar Pardesh       25.Uttarakhand')
    print('26.West Bengal           27.Telangana')
    print('\n_____________________________________________________________________________________________________')
    print('\n........................................Enter (0) for Exit..........................................\n')

    try:
      e=input('Enter The (State Name): ')
      if not re.match("[azAZ]$",e):
        print('')
      break
    except ValueError:
      print('Choose Accurate State NAME & (It Must Be Case Senstive).')
    finally:
      f=df[(df['Region']==e)]
      print(f.to_markdown())
      
      #x = np.arange(2)
      #y1 = [34, 56, 12, 89, 67]
      #y2 = [12, 56, 78, 45, 90]
      #y3 = [14, 23, 45, 25, 89]
     
        
      # plot data in grouped manner of bar type
      #plt.bar(x-0.2, y1, width, color='cyan')
      #plt.bar(x, y2, width, color='orange')
      #plt.bar(x+0.2, y3, width, color='green')
      # y1= df['x'].max()

      my_max = df[' Estimated Unemployment Rate (%)'].loc[df[' Estimated Unemployment Rate (%)'].idxmax()]      # Maximum in column
      my_min = df[' Estimated Labour Participation Rate (%)'].loc[df[' Estimated Labour Participation Rate (%)'].idxmin()]
      print('\n','Maximum Value',my_max)
      print('Minimum Value',my_min)

      plt.bar(my_max,width=0.8, alpha=0.5,color='red',height=0.6)
      plt.bar(my_min,width=0.8, alpha=0.5,color='blue',height=0.6)
      plt.show()
     
      
      
      

      print('\n.......................................Thank You...................................................')
      print('\n.....................................See You Soon..................................................')

