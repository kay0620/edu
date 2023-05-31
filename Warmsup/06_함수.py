def get_price(is_vip = False,
              is_birthday=False, 
              is_membership=False, 
              is_review=False, 
              first_time=False):
    price = 16000
    
    if is_vip == True:
        price -= 3000
    
    if is_birthday:
        price -= 1000
        
    if is_review:
        price -= 2000
        
    return price
    
    

def show_price(customer, is_vip=False,
              is_birthday=False, 
              is_membership=False, 
              is_review=False, 
              first_time=False):
    print(f'사랑하는 {customer} 고객님')    
    print('감성커트 가격은 {}원 입니다.(무릉도원 샴푸서비스)'.format(get_price(is_vip,is_birthday,is_membership, is_review, first_time)))


    
customer1 = '나장발'
show_price(customer1, is_review = True)

customer2 = '나수염'
show_price(customer2, is_birthday = True)

customer3 = '나푼젤'
show_price(customer3, is_vip = True)
