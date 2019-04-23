class Cipher():

  def encode(self, string, shift = 1):
    try:
      # redefine arguments
      while shift > 26:
        shift -= 26
      alphabet = list('abcdefghijklmnopqrstuvwxyz')
      def find_letter_idx(letter):
        return alphabet.index(letter)
      string = list(map(find_letter_idx, list(string.lower())))
      # perform shift operations
      res = []
      for num in string:
        if num + shift < 25:
          res.append(alphabet[num + shift])
        else: 
          res.append(alphabet[((num + shift) % 25) - 1])
      # return result
      return ''.join(res)
    except (err):
      raise Exception('An error occurred: ' + err)

  def decode(self, string, shift = 1):
    try:
      # redefine arguments
      while shift > 26:
        shift -= 26
      alphabet = list('abcdefghijklmnopqrstuvwxyz')
      def find_letter_idx(letter):
        return alphabet.index(letter)
      string = list(map(find_letter_idx, list(string.lower())))
      # perform shift operations
      res = []
      for num in string:
        if num - shift < 25:
          res.append(alphabet[num - shift])
        else: 
          res.append(alphabet[((num - shift) % 25) - 1])
      # return result
      return ''.join(res)
    except (err):
      raise Exception('An error occurred: ' + err)