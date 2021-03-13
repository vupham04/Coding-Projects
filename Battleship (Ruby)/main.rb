class Battleship
    @@board1 = Array.new(10){Array.new(10," ")}
    @@board2 = Array.new(10){Array.new(10," ")}
    @@boardPlay1 = Array.new(10){Array.new(10," ")}
    @@boardPlay2 = Array.new(10){Array.new(10," ")}
    @@player1 = 15
    @@player2 = 15
  
  
    def createTable(num)
      arr = @@board1
      if num==2
        arr = @@board2
      end
      puts "Create board for Player " + num.to_s
      shipInstalled = 0
      puts "Syntax: Position + h/v - h = Horizontal, v = Vertical (eg. 'A4 h' or 'B5 v')"
      while shipInstalled<5
        printBoard(num)
        if shipInstalled==0
          print "Enter the position that you want Carrier (5) installed: "
        elsif shipInstalled==1
          print "Enter the position that you want Battleship (4) installed: "
        elsif shipInstalled==2
          print "Enter the position that you want Cruiser (3) installed: "
        elsif shipInstalled==3
          print "Enter the position that you want Submarine (2) installed: "
        else
          print "Enter the position that you want Destroyer (1) installed: "
        end
        inputShip = gets.split(" ")
        temp = insertShip(arr, inputShip[0], inputShip[1], 5-shipInstalled)
        if temp==-1
          puts "Wrong move"
        else
          shipInstalled+=1
        end
      end
      printBoard(num)
    end
  
    def startGame
      player = 1
      while win==0
        puts "It's player " + player.to_s + " turn"
        board = @@board2
        boardPlay = @@boardPlay2
        if player==1
          printBoard(4)
        else 
          board = @@board1
          boardPlay = @@boardPlay1
          printBoard(3)
        end
        
        print "Enter the position that you want to sink: "
        pos = convertIndex(gets)
        res = sink(pos, board, boardPlay)
        if res==-1
          puts "Wrong move"
        else
          if res==1
            puts "Hit"
            if player==1
              @@player1 = @@player1-1
            else
              @@player2 = @@player2-1
            end
          else
            puts "Missed"
          end
          if player==1
            player = 2
          else
            player=1
          end
        end
      end
      if @@player1==0
        puts "Player 1 wins"
      else
        puts "Player 2 wins"
      end
    end
  
    def sink(position, board, boardPlay)
      if position[0]==-1
        return -1
      elsif boardPlay[position[0]][position[1]]!=' '
        return -1
      else
        if board[position[0]][position[1]]=='X'
          boardPlay[position[0]][position[1]] = 'H'
          return 1 # hit
        else 
          boardPlay[position[0]][position[1]] = 'M'
          return 0 #missed
        end
      end
    end
  
    def insertShip(board, position, side, leng)
      index = convertIndex(position)
      # check if it's possible to put the ship there
      if index[0]==-1
        return -1
      end
      # if it is horizonal
      if side=="h"
        # check if it's possible to put the ship there
        if index[1]+leng-1>9
          return -1
        end
        for i in index[1]..index[1]+leng-1
          if board[index[0]][i]=='X' # check if there is any ship already there
            return -1
          end
        end
        #mark the board
        for i in index[1]..index[1]+leng-1
          board[index[0]][i]='X'
        end
      # if it is vertical
      elsif side=="v"
        # check if it's possible to put the ship there
        if index[0]+leng-1>9
          return -1
        end
        for i in index[0]..index[0]+leng-1
          if board[i][index[1]]=='X' # check if there is any ship already there
            return -1
          end
        end
        #mark the board
        for i in index[0]..index[0]+leng-1
          board[i][index[1]]='X'
        end
      # wrong syntax
      else
        return -1
      end
      #success
      return 0
    end
  
    def win
      if @@player1==0 or @@player2==0
        return 1
      else
        return 0
      end
    end
  
    def printBoard(num)
      arr = @@board1
      
      if num==2
        arr = @@board2
      elsif num==3
        arr = @@boardPlay1
      elsif num==4
        arr = @@boardPlay2
      end
      puts "   |  A|  B|  C|  D|  E|  F|  G|  H|  I|  J|"
      for i in 0..9
        temp = arr[i]
        if i==9
          puts (i+1).to_s+" |  " + temp.join('|  ') + '|'
        else  
          puts " "+(i+1).to_s+" |  "+ temp.join('|  ') + '|'
        end
      end
    end
  
    def convertIndex(input)
      a = input[0].ord-65
      b = input[1, input.length-1].to_i-1
      if a<0 or a>9 or b<0 or b>9
        return [-1]
      end
      return [b,a]
    end
  
  end
  
  b = Battleship.new
  b.createTable(1)
  b.createTable(2)
  b.startGame