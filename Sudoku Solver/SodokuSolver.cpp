#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    bool findLocation(vector<vector<char>> &board, int &row, int &col){
        for(int i = 0 ; i<9 ; ++i){
            for(int j = 0 ; j < 9; ++j){
                if(board[i][j] == '.'){
                    row = i;
                    col = j;
                    return true;
                }
            }
        }
        return false;
    }
    
    bool isValidRow(vector<vector<char>> &board, int row, char num){
        for(int i = 0;  i<9 ; ++i){
            if(board[row][i] == num )
                return false;
        }

        return true;
    }
    
    bool isValidCol(vector<vector<char>> &board, int col, char num){
        for(int i = 0; i<9 ; ++i){
            if(board[i][col] == num)
                return false;
        }
        
        return true;
    }
    bool isValidGrid(vector<vector<char>> &board, int col, int row, char num){
        int rowKey = row - row%3;
        int colKey = col - col%3;
        for(int i = 0 ; i < 3 ; ++i){
            for(int j = 0 ; j < 3; ++j ){
                if(board[i+rowKey][j+colKey] == num)
                    return false;
            }
        }

        return true;
    }
    bool isValid(vector<vector<char>> &board, int col, int row , char num){
        return isValidRow(board,row,num) and isValidCol(board,col,num) and                      isValidGrid(board,col,row,num);
    }
    
    bool Helper(vector<vector<char>> &board){
        int row, col;
        if(!findLocation(board,row,col))
            return true;
        for(int i=1 ; i < 10 ; i++){
            if(isValid(board,col,row,char(i+'0'))){
                board[row][col] = char(i+'0');
                if(Helper(board))
                    return true;
                board[row][col] = '.';
            }
        }
        return false;
    }
    
    void solveSudoku(vector<vector<char>>& board) {
        Helper(board);
    }
};