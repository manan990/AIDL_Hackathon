#  const timeRegexArray = [
#     /((([0-9]{2})|([0-9])):[0-9]{2}:[0-9]{2}) (pm|am)/gi,
#     /((([0-9]{2})|([0-9])):[0-9]{2}) (pm|am)/gi,
#     /((([0-9]{2})|([0-9])):[0-9]{2}:[0-9]{2})/gi,
#     /((([0-9]{2})|([0-9])):[0-9]{2})([0-9]{2}:[0-9]{2})/gi,
#     /((([0-9]{2})|([0-9])):[0-9]{2})/gi
#   ];

#  const dateRegexArray = [
#      / ([0-2][0-9] | (3)[0-1] | [0-9])(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)\d{4}/gi,
#      / (((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)([0-2][0-9] | (3)[0-1] | [0-9])(\/ |\. |\-)\d{4}/gi,
#      / (([0-9]) | ([0-2][0-9]) | ([3][0-1]))(\/ |\. |\-)(Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec)(\/ |\. |\-)\d{4}/gi,
#      / (Jan | Feb | Mar | Apr | May | Jun | Jul | July | Aug | Sep | Oct | Nov | Dec)(\/ |\. |\-)(([0-9]) | ([0-2][0-9]) | ([3][0-1]))(\/ |\. |\-)\d{4}/gi,
#      /\d{4}(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)([0-2][0-9] | [0-9] | (3)[0-1])/gi,
#      /\d{4}(\/ |\. |\-)([0-2][0-9] | [0-9] | (3)[0-1])(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])/gi,

#      / ([0-2][0-9] | (3)[0-1] | [0-9])(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)\d{2}/gi,
#      / (((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)([0-2][0-9] | (3)[0-1] | [0-9])(\/ |\. |\-)\d{2}/gi,
#      / (([0-9]) | ([0-2][0-9]) | ([3][0-1]))(\/ |\. |\-)(Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec)(\/ |\. |\-)\d{2}/gi,
#      / (Jan | Feb | Mar | Apr | May | Jun | Jul | July | Aug | Sep | Oct | Nov | Dec)(\/ |\. |\-)(([0-9]) | ([0-2][0-9]) | ([3][0-1]))(\/ |\. |\-)\d{2}/gi,
#      /\d{2}(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])(\/ |\. |\-)([0-2][0-9] | [0-9] | (3)[0-1])/gi,
#      /\d{2}(\/ |\. |\-)([0-2][0-9] | [0-9] | (3)[0-1])(\/ |\. |\-)(((0)[0-9]) | ((1)[0-2]) | [0-9])/gi
#  ]