# Hangman Strategy (N-gram Approach)

## Overview
This folder contains a small project exploring strategies to play the game of **Hangman**.  
The goal is to move beyond random or simple frequency-based guesses by using a **probability model of letter sequences**.

## Method
- **N-gram language model**: builds frequency tables from a training dictionary at different lengths (1-gram to 7-gram).  
- **Back-off smoothing**: longer N-grams are preferred when available; if not, the algorithm falls back to shorter ones.  
- **Pattern matching**: for a masked word (e.g., `_a__m_n`), the model evaluates candidate letters against all consistent contexts.  
- **Decision rule**: select the letter with the highest probability; if all are zero, guess randomly among unused letters.  
- **Yesterday’s experiment notebook** (`hangman_api_user.ipynb`) demonstrates the guessing process and evaluates win rate.  

## Results
- The N-gram strategy consistently outperforms baseline letter-frequency guessing.  
- It is especially effective for longer words where context information is richer.
- Achieve a out-of-sample accuracy of 60%+

## Files
- `hangman_api_user.ipynb` — notebook showing how the strategy works and testing it on sample words.  
- `Hangman_Strategy Description.docx` — a short document describing the reasoning behind the algorithm.  

## Notes
This is a **mini project for practice** in probabilistic modeling and algorithm design, not a full production system.  
It demonstrates how ideas from language modeling can be applied to game strategies in a compact, educational setting.
