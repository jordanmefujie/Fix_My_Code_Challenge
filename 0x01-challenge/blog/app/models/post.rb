class Post < ApplicationRecord
  has_many  :comments, dependent: :destroy
  validates :title, presence: true, length: {minimum: 5}
  validates_inclusion_of :online, in: [true, false]
	validates :body,  presence: true
end
